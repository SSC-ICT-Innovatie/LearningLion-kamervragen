# Docs

Voor het maken van de documentatie wordt gebruik gemaakt van Sphinx.

Sphinx leest de .py-bestanden en genereert op basis daarvan een website met alle documentatie uit de code. Hierbij wordt gelet op docstrings (documentatie in de code). Een voorbeeld van een docstring is:

```py
    def fetchFile(self, fileId):
        """
        Fetches the file with the given fileId
        
        :param fileId: The id of the file to be fetched
        """
        pass
```

Het genereren van documentatie is vrij eenvoudig. We gebruiken de map _docs, waarin een submap source aanwezig is. In deze map worden bestanden opgeslagen om te indexeren. Deze bestanden worden aangemaakt met behulp van het volgende commando:

``sphinx-apidoc -o _docs/source/ ../``

Om de documentatie daadwerkelijk te genereren (inclusief indexeren en het omzetten naar HTML), gebruik je het commando: ``make html`` Het is altijd verstandig om vooraf het volgende commando uit te voeren:  ``make clean`` Hiermee verwijder je oude documentatie, zodat er geen conflicten ontstaan.