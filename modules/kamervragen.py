"""
    Dit is een module voor kamervragen.
"""

from flask import jsonify
from DataFetcher.libraries.data_classes.range_enum import Range
from DataFetcher.run_local import run_local_datafetcher
from inference.run_local import infer_run_local
from ingester.libraries.database import Database
from ingester.libraries.embedding import Embedding
from ingester.run_local import run_local_ingest_stores
from querier.run_local import run_local_query_stores


class KamerVragenModule:
    def initialize(app, data):
        """
            initaliseer kamervragen dit bevat: 
            - het ophalen
            - het verwerken
            van documenten
        """
        try:
            # Standaard is de range tiny
            range = Range.Tiny
            if "range" in data:
                if data["range"] not in Range.__members__:
                    return jsonify({"error": "Invalid range"})
                range = Range[data["range"]]
            run_local_datafetcher(range=range)
            run_local_ingest_stores()
            return jsonify({"status": "success"})
        except Exception as e:
            return jsonify({"error": str(e)})

    def inference(
        app,
        data,
        defaultRange=Range.Tiny,
        model="BramVanroy/fietje-2-chat",
        systemPrompt=None,
        noOllama=False,
    ):
        """
            Voer een inference uit op de LLM
        """
        files = []
        _range = defaultRange
        fetchedFiles = []
        ministersentiment = ""
        nieuwsfeiten = ""
        inleiding = ""
        print("Data: ", data)
        if "range" in data:
            if data["range"] not in Range.__members__:
                return jsonify({"error": "Invalid range"})
            _range = Range[data["range"]]
            app.logger.info(f"Using range: {_range.name}")
        if "files" in data:
            # Als er bestanden zijn worden deze eerst opgehaald zodat het taalmodel deze kan gebruiken
            embeddings = Embedding()
            database = Database(embed=embeddings, range=_range)
            files = data["files"]
            print(f"Files: {files}")
            for file in files:
                print(f"uuid {file.get('uuid')}")
                database.get_database_connection()
                # get answer from database
                fetchedData = database.getQuestion(
                    file.get("uuid"), file.get("questionNumber")
                )
                fetchedFiles.append(fetchedData)
            app.logger.info(f"Question and answer: {fetchedFiles}")
        message = {}
        if "message" in data:
            # Als er een message is wordt deze gebruikt om de context te bepalen
          print("message is found")
          message = data["message"]
          print(f"Message: {message}")
        if "departmentSentiment" in message:
            # Als er een sentiment is wordt deze gebruikt om de context te bepalen
            ministersentiment = message["departmentSentiment"]
            app.logger.info(f"departmentSentiment: {ministersentiment}")
        if "news" in message:
            # Als er nieuws is wordt deze gebruikt om de context te bepalen
            nieuwsfeiten = message["news"]
            app.logger.info(f"news: {nieuwsfeiten}")
        if "inleiding" in message and "vragen" in message:
            # Als er een inleiding en vragen zijn wordt deze gebruikt om de context te bepalen
            inleiding = message["inleiding"]
            data["prompt"] = f"{message['inleiding']} {message['vragen']}"
        app.logger.info(f"Prompt: {data['prompt']}")
# De system prompt
        systemPrompt = f"""
You are a RAG assistant. Je beantwoord vragen uit de prompt op basis van informatie die je krijgt uit eerdere beantwoordingen.
Houd je nauwkeurig aan de context. Verzin geen informatie die je niet weet (don't hallucinate). Als je onvoldoende informatie hebt om de vragen te beantwoorden, antwoord je met:
"Ik heb onvoldoende informatie om de vragen te beantwoorden."
Je antwoordt vanuit de rol van minister.
De informatie welke je kunt gebruiken voor de beantwoording (je context) is:
- Het standpunt van de minister: {ministersentiment},
- Relevante nieuwsfeiten: {nieuwsfeiten}
- Relevante eerder beantwoordde kamervragen: {fetchedFiles}
end information / context
Je antwoordt per vraag in een korte alinea.
Voorbeeld:
Vraag 4
Zou u willen reflecteren op de conclusie van het rapport dat de aanwezige politiemensen bij het tankstation in Meppel onvoldoende bescherming hebben geboden aan demonstranten terwijl ze klemgereden en aangevallen werden (onder andere met vuurwerk)?
Antwoord 4
Er wordt erkend door de politie dat er fouten zijn gemaakt bij deze demon-stratie. Zoals benoemd in vraag 1 heeft de korpschef mij laten weten dat de politie zich herkent in de kritiekpunten die naar voren zijn gekomen in het rapport van de Inspectie.
Vraag 5
Zijn er relschoppers aangemerkt als verdachte van deze strafbare gedragin-gen? Zo nee, bent u bereid om na de publicatie van dit rapport het Openbaar Ministerie hiertoe opdracht te geven om verder onderzoek te doen? Zou u uw antwoord willen toelichten?
Antwoord 5
Het Openbaar Ministerie gaat vier personen vervolgen. Deze vier personen moeten zich op 16 januari 2024 verantwoorden voor de rechter.
Vraag 6
Hoe kijkt u naar de uitlatingen van politiemensen bij het tankstation in Meppel die tegen demonstranten zeiden: «als jullie niet weggaan zijn de risico’s voor jullie zelf», en vervolgens wegreden? Zijn deze politiemensen disciplinair gestraft? Zo nee, bent u bereid om de politie te vragen om een disciplinair onderzoek te starten naar deze agenten?
etc.
-einde voorbeeld-
Je geeft dus per subvraag uit de user prompt de vraag terug met het bijbehorende antwoord.
De inleiding (met het thema) van de kamervraag is {inleiding}

Genereer altijd in het nederlands!
"""


        filename = None
        if ',' in model:
            # als het model een , bevat dan wordt deze gesplitst (dit was nodig voor de guff mogelijkheid)
            model = model.split(',')
            filename = model[1]
            model = model[0]

        # Roep de inferentie aan
        AIresponse = infer_run_local(
            data["prompt"], files=fetchedFiles, systemPrompt=systemPrompt, LLM=model, filename=filename, noOllama=noOllama
        )
        app.logger.info(f"AI response: {AIresponse}")
        return jsonify({"prompt": data["prompt"], "output": AIresponse})

    def query(app, data, range=Range.Tiny):
        """
            Voer een query uit op de databases
        """
        _range = range
        if "range" in data:
            if data["range"] not in Range.__members__:
                return jsonify({"error": "Invalid range"})
            _range = Range[data["range"]]
        app.logger.info(f"Using range: {range.name}")
        app.logger.info(f"Using range: {_range.name}")
        print("USING RANGE ", _range)
        documents = run_local_query_stores(data["query"],data["subject"], range=_range)
        app.logger.info(f"Documents: {documents}")
        return jsonify({"query": data["query"], "documents": documents})
