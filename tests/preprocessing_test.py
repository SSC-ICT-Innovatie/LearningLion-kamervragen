import unittest

from ingester.libraries.preprocessor import Preprocessor

class IngesterTest(unittest.TestCase):

	whole_doc = """
# 2

#### Vergaderjaar 2023–2024 Aanhangsel van de Handelingen

**Vragen gesteld door de leden der Kamer, met de daarop door de**
**regering gegeven antwoorden**

### 387

Vragen van het lid Boswijk (CDA) aan de Minister van Buitenlandse Zaken
over de situatie in de Zuidelijke Kaukasus (ingezonden 2 oktober 2023).

Antwoord van Minister Bruins Slot (Buitenlandse Zaken) (ontvangen
13 november 2023).

Vraag 1
Bent u bekend met de recente berichtgeving omtrent Nagorno-Karabach, in
het bijzonder de commentaren «Netjes gezuiverd»[1 ] en «Goede bedoelingen
van de EU zijn weinig waard als de harde machtsverhoudingen verschuiven»[2]?

Antwoord 1
Ja.

Vraag 2
In hoeverre kan er worden gesproken van een etnische zuivering in NagornoKarabach? Deelt u de opvatting dat Nagorno-Karabach weliswaar niet met
geweld etnisch wordt gezuiverd, maar dat de oorspronkelijke bewoners van
het gebied vanwege de serieuze geweldsdreigingen, de uithongeringstactieken en de bedreigende taal van de Azerbeidzjaanse president Alijev geen
andere keuze hebben dan te vertrekken en dat er in die zin weldegelijk sprake
is van een etnische zuivering? En wat betekent deze constatering voor het
handelingskader van de Europese Unie (EU) jegens Azerbeidzjan?

Antwoord 2
Het leidt geen twijfel dat de etnisch Armeense bewoners van NagornoKarabach het gebied zijn ontvlucht omdat zij zich niet veilig voelden, o.a.
vanwege de maandenlange blokkade van de Lachin-corridor. Of er gesproken
kan worden van een etnische zuivering is een juridisch ingewikkelde kwestie.
Het kabinet zal in een separate brief op deze vraag ingaan, mede in het kader
van de aangenomen motie van het Lid Ceder over op basis van feiten


1 Nederlands Dagblad, 29 september 2023, «De ondergang van Nagorno Karabach is verbonden
met het wegkijken van de EU» (De ondergang van Nagorno Karabach is verbonden met het
wegkijken van de EU – Nederlands Dagblad. De kwaliteitskrant van christelijk Nederland).

2 De Volkskrant, 20 september 2023, «Goede bedoelingen van de EU zijn weinig waard als de
harde machtsverhoudingen verschuiven» (Goede bedoelingen van de EU zijn weinig waard als
de harde machtsverhoudingen verschuiven (volkskrant.nl)).


h tk 20232024 387


-----

(12-10-2023).[3 ]

Vraag 3
Klopt het dat u recent met de Hoge vertegenwoordiger van de Unie voor
buitenlandse zaken en veiligheidsbeleid heeft gesproken over de situatie in
Nagorno-Karabach? Zo ja, kunt u schetsen wat de komende periode de
Europese inzet wordt richting Azerbeidzjan? Worden er sancties ingesteld
tegen degenen die de gedwongen exodus hebben vormgegeven?

Antwoord 3
Het klopt dat ik hierover, op 27 september jl., met de Hoge Vertegenwoordiger heb gesproken. Daarnaast is tijdens de Raad Buitenlandse Zaken (RBZ)
van 23 oktober jl. ook kort gesproken over deze situatie.
HV Borrell stelde tijdens de RBZ ten aanzien van steun voor Armenië voor dat
EDEO de mogelijkheden voor non-lethale steun onder de Europese Vredesfaciliteit (EPF) zorgvuldig zal verkennen. Hetzelfde geldt voor de mogelijkheden
om de Europese Unie Missie in Armenië (EUMA) te versterken met meer
mensen en meer patrouilles. EDEO zal voorts, met een missie naar Armenië,
de mogelijkheden voor economische steun in kaart brengen. Nederland heeft
conform de motie van het lid Ceder[4 ] in de Raad steun uitgesproken voor
bovenstaande ideeën en andere EU-lidstaten opgeroepen dit ook te doen.
Tevens heeft Nederland conform de motie van leden Bikker en Omtzigt
aangegeven dat in geval van nieuw geweld binnen de EU gesproken moet
worden over gepaste maatregelen.[5 ] De HV gaf aan dat de Armeense Minister
van Buitenlandse Zaken uitgenodigd zal worden voor de RBZ van november.

Vraag 4 en 5
Deelt u de zorg dat Azerbeidzjan mogelijk op korte termijn militair een
doorgang zal proberen te forceren naar de Azerbeidjaanse exclave
Nachitsjevan, hetgeen een grove schending van het internationaal recht zou
betekenen?
Hoe wordt door de Europese Unie geanticipeerd op deze mogelijke
geweldsescalatie? Welke maatregelen worden voorbereid indien Azerbeidzjan
besluit Armenië binnen te vallen?

Antwoord 4 en 5
In het trilaterale akkoord van 2020 is expliciet vermeld dat alle economische
en transportverbindingen van en naar Nachitsjevan gedeblokkeerd worden,
welke onbelemmerd verkeer van personen, voertuigen en vracht in beide
richtingen zou bewerkstelligen.
Het kabinet heeft momenteel geen aanwijzingen dat Azerbeidzjan plannen
heeft om een doorgang te forceren naar de exclave Nachitsjevan.
Azerbeidzjan heeft publiekelijk bevestigd dat het de route naar Nachitsjevan
met en via Iran verder wil ontwikkelen. Nederland en de EU blijven inzetten
op het zo snel mogelijk hervatten van de vredesonderhandelingen tussen
Armenië en Azerbeidzjan, ook om wederzijdse erkenning van de Armeense en
Azerbeidzjaanse territoriale integriteit expliciet vast te leggen. Wat betreft
maatregelen in geval van nieuw geweld zij verwezen naar mijn interventie
tijdens de RBZ van 23 oktober jl., zie ook het antwoord op vraag 3.

Vraag 6
Kunt u uiteenzetten in welke mate de Europese Unie afhankelijk is van
Azerbeidjaans gas en hoe deze afhankelijkheid er de komende jaren uit gaat
zien indien er geen koerswijziging plaatsvindt?

Antwoord 6
In juli 2022 heeft de voorzitter van de Europese Commissie Ursula Von der
Leyen een memorandum van overeenstemming getekend met Azerbeidzjan
om de gasexport naar de EU te verdubbelen. Dit is in lijn met de EU-inzet

3 Kamerstuk 21 501-02, nr. 2733
4 Motie Ceder, Kamerstuk 21 501-02, nr. 2732
5 Motie Bikker en Omtzigt, Kamerstuk 36 410, nr. 31


-----

4% van het totale EU-verbruik aan gas vanuit Azerbeidzjan. Nederland
importeert geen Azerbeidzjaans gas.[6 ]

Vraag 7
Wordt er naar aanleiding van de recente gebeurtenissen in Azerbeidzjan al
actief gezocht naar vervanging van Azerbeidjaans gas? Zo nee, waarom niet,
en kunt u dit als voorstel op tafel leggen tijdens de eerstvolgende Raad
Buitenlandse Zaken?

Antwoord 7
De EU beraadt zich momenteel allereerst op de wijze waarop Armenië
gesteund kan worden. Hierover is kort gesproken tijdens de Raad Buitenlandse Zaken (RBZ) van 23 oktober jl. Zoals vermeld in het verslag van de
RBZ stelde de Hoge Vertegenwoordiger Borrell in dit kader voor dat EDEO de
mogelijkheden voor non-lethale EPF zorgvuldig zal verkennen. Hetzelfde geldt
voor de mogelijkheden om de Europese Unie Missie in Armenië (EUMA) te
versterken met meer mensen en meer patrouilles. EDEO zal voorts, met een
missie naar Armenië, de mogelijkheden voor economische steun in kaart
brengen. Nederland heeft conform de motie van het lid Ceder[7 ] in de Raad
steun uitgesproken voor bovenstaande ideeën en andere EU-lidstaten
opgeroepen dit ook te doen. Tevens heeft Nederland conform de motie van
leden Bikker en Omtzigt aangegeven dat in geval van nieuw geweld binnen
de EU gesproken moet worden over gepaste maatregelen[8].

Vraag 8
Welke maatregelen heeft de Europese Unie inmiddels getroffen tegen
doorvoerland Azerbeidzjan naar aanleiding van het 11e sanctiepakket?

Antwoord 8
Azerbeidzjan heeft de aandacht van de EU en Nederland als het gaat om
omzeiling. Op dit moment is er geen concrete aanleiding voor specifieke
maatregelen ten aanzien van Azerbeidzjan. In algemene zin geldt dat met het
11[e ] sanctiepakket een belangrijk signaal is gegeven dat de EU de omzeiling
van sancties stevig aanpakt. Er zijn exportbeperkingen opgelegd tegen
bedrijven uit VAE, Oezbekistan en Hongkong wegens betrokkenheid bij
omzeiling.
Ook is er een stappenplan opgenomen voor de aanpak van omzeiling,
bestaande uit (1) het intensiveren van samenwerking met derde landen door
diplomatieke outreach, (2) passende individuele maatregelen tegen marktdeelnemers uit derde landen betrokken bij het faciliteren van omzeiling en
(3) in het uiterste geval de mogelijkheid tot opleggen exportrestricties voor
een land als geheel. Besluitvorming hierover geschiedt met unanimiteit,
voorafgegaan door grondige analyse, inclusief reeds ondernomen acties en
voorwaarde dat het land in kwestie is geïnformeerd en geconsulteerd.
Nederland steunt EU-sanctiegezant O’Sullivan in zijn diplomatieke inspanningen gericht op derde landen waar omzeiling plaatsvindt en met analyses die
bijdragen aan het bovengenoemde stappenplan.

Vraag 9
Welke noodhulp verlenen Nederland en de Europese Unie aan Armenië maar
aanleiding van de recente gebeurtenissen en welke mogelijkheden ziet u om
dit verder op te schalen?

Antwoord 9
In de brief op verzoek van uw Kamer d.d. 11 oktober 2023 (Kamerstuk
21 501-02, nr. 2737) gaat het kabinet nader in op de internationale hulpverlening en de Nederlandse bijdrage daaraan in Nagorno-Karabach en in
Armenië. Het kabinet heeft zich in internationaal verband ingezet voor
onbelemmerde humanitaire toegang tot Nagorno-Karabach. Ook stelt het

6 Gegevens ENTSOG, Enerdata.net
7 Motie Ceder, Kamerstuk 21 501-02 nr. 2732
8 Motie Bikker en Omtzigt, Kamerstuk 36 410, nr. 31


-----

de Rode Halve Maan. Deze financiering stelt hulporganisaties in staat om snel
te reageren op rampen en crises, zoals in Nagorno-Karabach en Armenië.
Onder meer de VN-vluchtelingenorganisatie UNHCR, UNICEF, het Internationale Comité van het Rode Kruis (ICRC) en de Internationale Federatie van het
Rode Kruis en de Rode Halve Maan (IFRC) zijn, mede dankzij deze Nederlandse financiering, actief. Het VN Central Emergency Response Fund,
waarvan Nederland dit jaar de grootste donor is, heeft 4 miljoen euro
beschikbaar gesteld voor de respons. Ook draagt de Europese Commissie bij
aan de hulpverlening, o.a. door middel van een financiële bijdrage van 10
miljoen euro en een EU-humanitaire luchtbrug.

Vraag 10
Kunt u in de beantwoording van deze vragen ook ingaan op de voortgang die
wordt geleverd naar aanleiding van de motie van de leden Bikker en Omtzigt
(Kamerstuk 36 410, nr. 74)?

Antwoord 10
Het kabinet heeft, conform motie Bikker/Omtzigt (Kamerstuk 36 410, nr. 74), in
EU-kader erop aangedrongen maatregelen tegen Azerbeidzjan te bespreken.
Tijdens de Raad Buitenlandse Zaken (RBZ) van 23 oktober jl. heeft Nederland
aangegeven dat in geval van nieuw geweld binnen de EU gesproken moet
worden over gepaste maatregelen[9].

9 Motie Bikker en Omtzigt, Kamerstuk 36 410, nr. 31


-----

"""
	whole_doc2 = """
 # 2

#### Vergaderjaar 2023–2024 Aanhangsel van de Handelingen

**Vragen gesteld door de leden der Kamer, met de daarop door de**
**regering gegeven antwoorden**

### 302

Vragen van het lid Dijk (SP) aan de Minister voor Langdurige Zorg en Sport
over antwoord op de vragen inzake de uitzending «Het geheim van de
_spreekkamer» en het artikel «Zorgverzekeraars hebben groot belang bij de data_
_die toezichthouder verzamelt» en Peiling MIND: meerderheid cliënten niet_
_geïnformeerd over gegevensdeling met de NZa (ingezonden 3 oktober 2023)._

Antwoord van Minister Helder (Langdurige Zorg en Sport) (ontvangen
24 oktober 2023).

Vraag 1
Wat is uw reactie op de uitslag van de peiling van MIND dat 74% van de
respondenten niet via de hulpverlener geïnformeerd is over het feit dat
gegevens worden doorgegeven en dat 72% van de respondenten niet is
gewezen op de mogelijkheid om een zogeheten privacyverklaring in te
vullen?[1 ]

Antwoord 1
Ik vind dit onwenselijk. Ik verwacht van zorgaanbieders dat zij hun cliënten en
patiënten over de privacyverklaring goed, volledig en neutraal informeren, de
keuze altijd helemaal bij de patiënt laten en daar geen invloed op uitoefenen.
De Nederlandse Zorgautoriteit (NZa) heeft ter ondersteuning ook een
informatiefolder opgesteld om cliënten en patiënten te informeren.[2 ] De NZa
heeft bij mij aangegeven deze patiëntenfolder actief te delen met zorgaanbieders, zodat zij cliënten en patiënten op hun beurt kunnen informeren. Naar
aanleiding van berichtgeving in verschillende media over privacy in het licht
van de data-uitvraag van de NZa voor de zorgvraagtypering heeft de NZa ook
extra aandacht besteed aan privacy in de geestelijke gezondheidszorg (ggz)
via hun website.[3 ] Dit alles om cliënten en patiënten zo goed mogelijk te
informeren en in staat te stellen om de keuze te maken of zij willen dat hun
gegevens met de NZa worden gedeeld.


1 Aanhangsel van de Handelingen, vergaderjaar 2023–2024, nr. 76 (2023D39037); Mind Platform,
31 augustus 2023, «Peiling Mind: Meerderheid cliënten niet geïnformeerd over gegevensdeling
met NZa» – Peiling MIND: meerderheid cliënten niet geïnformeerd over gegevensdeling met
NZa (mindplatform.nl).

2 https://puc.overheid.nl/nza/doc/PUC_743104_22/1/.
3 Privacy in de ggz | Geestelijke gezondheidszorg (ggz) en forensische zorg (fz) | Nederlandse
Zorgautoriteit (nza.nl).


h tk 20232024 302


-----

van een zogeheten privacyverklaring voor cliënten in de ggz (geestelijke
gezondheidszorg) algemeen bekend is? Zo ja, op basis van welke gegevens
baseert de NZa dit, aangezien zij niet monitort hoe goed ggz-patiënten
bekend zijn met de privacyverklaring in de ggz?

Antwoord 2
De NZa geeft bij mij aan dat gegevensdeling in de zorg niet nieuw is. Daarom
gaat de NZa er van uit dat zorgaanbieders de uitvraag rond zorgvraagtypering onderdeel hebben gemaakt van het gesprek dat zij voeren over
gegevensdeling met cliënten en patiënten. De NZa heeft mij laten weten dat
de hier bedoelde privacyverklaring ook al sinds 2014 bestaat en er daarom
vanuit gaat dat zorgverleners bekend zijn met deze privacyverklaring. Zoals
bij het antwoord op vraag 1 aangegeven verwacht ik daarbij dat zorgaanbieders hun patiënten zo goed mogelijk, neutraal en in begrijpelijke taal
informeren over de privacyverklaring en het verzamelen van hun zorg- en
behandelgegevens door de NZa, zodat deze zelf een beslissing kunnen
nemen over het delen van hun gegevens met de NZa door hun zorgverlener.

Vraag 3
Klopt het dat bij het ondertekenen van de eerdergenoemde privacyverklaring
niet alleen het delen van de gegevens met de NZa wordt stopgezet, maar ook
het delen van gegevens met de desbetreffende zorgverzekeraar? Waarom is
er destijds geen aparte privacyverklaring ontwikkeld die alleen over het delen
van gegevens met de NZa gaat?

Antwoord 3
Het klopt dat de privacyverklaring geldt voor verzending van gegevens aan
zowel zorgverzekeraars als aan de NZa. De NZa heeft mij laten weten in 2021
en 2022 onderzocht te hebben of het mogelijk was de privacyverklaring op te
splitsen, zodat kon worden aangegeven welke partij of welke set gegevens
niet mogen inzien. Gegevensdeling is echter zeer afhankelijk van de
ICT-infrastructuur bij zorgaanbieders. De partijen die de ICT-systemen van
zorgaanbieders verzorgen gaven in dit kader aan de NZa aan dat het
onmogelijk was deze splitsing (tijdig) gerealiseerd te krijgen.

Vraag 4
Zijn er gevallen bekend waarbij gegevens van ggz-cliënten die een privacyverklaring hadden ondertekend alsnog doorgegeven zijn door de ggzinstelling aan de NZa? Zo ja, om hoeveel gevallen gaat het?

Antwoord 4
Het aanleveren van de medisch-inhoudelijke gegevens wanneer een patiënt
een privacyverklaring heeft ondertekend is expliciet uitgesloten in de
Regeling ggz en fz en in de aanleverstandaard zorgvraagtypering.[4 5 ] De NZa
geeft bij mij aan de eigen systemen zo georganiseerd te hebben dat het
onmogelijk is de uitgesloten gegevens van een patiënt te ontvangen wanneer
in de aanlevering is aangegeven dat er sprake is van een privacyverklaring.
Uit een recente test blijkt dan ook dat er geen medisch-inhoudelijke gegevens
aanwezig zijn voor patiënten bij wie is aangegeven dat zij een privacyverklaring hebben ondertekend.
Eerder is wel gebleken dat één ICT-systeem niet in alle gevallen aangaf dat er
een privacyverklaring was ondertekend door een probleem in de programmatuur van dat ICT-systeem. Zodra de NZa hier een signaal over ontving is zij in
overleg getreden met de ICT-leverancier en heeft verzocht bij haar klanten, de
zorgaanbieders, na te gaan of het probleem zich bij hen had voorgedaan. De
NZa heeft bij mij aangegeven van in totaal vijf zorgaanbieders het signaal te
hebben ontvangen dat dit probleem zich ook bij hen heeft voorgedaan. De
NZa heeft vervolgens de bestanden waarin deze fout zat verwijderd en heeft

4 Standaard voor gegevensaanlevering zorgvraagtypering (ggz & fz) – versie 1.3 – Nederlandse
Zorgautoriteit (overheid.nl).

5 Regeling geestelijke gezondheidszorg en forensische zorg – NR/REG-2313a – Nederlandse
Zorgautoriteit (overheid.nl).


-----

Vraag 5
Welke procedure treedt er bij de NZa in werking als blijkt dat een ggzinstelling onterecht gegevens heeft doorgegeven van cliënten die een
privacyverklaring hadden ondertekend?

Antwoord 5
De NZa geeft bij mij aan géén gegevens te willen verwerken die zij niet mag
verwerken. Om die reden wordt de aanlevering van de gegevens van
patiënten waarbij bekend is dat dat ze privacyverklaring hebben ondertekend
automatisch afgewezen en verwijderd, zoals ook aangegeven in antwoord op
vraag 4. De zorgaanbieder ontvangt hiervan bericht met het verzoek de
gegevens aan te passen en opnieuw aan te leveren.
Als het voorkomt dat de automatische veiligheidsmechanismen niet in
werking treden, omdat in het bestand van de zorgaanbieder niet wordt
aangegeven dat er sprake is van een privacyverklaring terwijl dat wel het
geval is, neemt de NZa direct contact op met de betreffende ICT-leverancier.
De NZa verwijdert deze bestanden en verzoekt de gegevens opnieuw aan te
leveren zonder de gegevens van patiënten die een privacyverklaring hebben
ondertekend, zoals ook bij vraag 4 toegelicht. De NZa heeft onderzoek gedaan
of dit soort situaties met extra automatische of menselijke interventies
voorkomen kunnen worden. Dit blijkt helaas niet het geval volgens de NZa,
omdat de fout zit in de ICT-systemen waaruit de bestanden worden aangeleverd.

Vraag 6
Hoe komt het dat in uw brief van 13 april 2023 over het zorgprestatiemodel
en de zorgvraagtypering[6 ] het argument van het terugdringen van de
wachttijden in de ggz niet genoemd werd, terwijl dit nu wel als belangrijkste
argument wordt gebruikt door de NZa voor de data-uitvraag voor de
zorgvraagtypering?[7 ]

Antwoord 6
In de brief van 13 april 2023 bent u geïnformeerd over de uitkomsten van de
eerste evaluatie van het zorgprestatiemodel, hierin heb ik expliciet stilgestaan
bij de toegankelijkheid van de ggz: «Dit [het zorgprestatiemodel] draagt bij
_aan een goede ggz, die toegankelijk is voor iedereen die haar nodig heeft.»_
Een goede ggz die toegankelijk is, is voor mij een ggz die de wachttijden
weet terug te dringen en zo mensen tijdig en goed zorg kan bieden. Ik heb in
deze brief, zij het in iets andere bewoordingen, dus weldegelijk het argument
van terugdringen van wachttijden aangehaald als belangrijke reden voor
invoering van zorgprestatiemodel en de daarmee samenhangende dataverzameling.

Vraag 7
Wat zijn volgens u de oorzaken van de lange wachttijden in de ggz?

Antwoord 7
Hiervoor zijn meerdere redenen. De druk op de ggz is al langere tijd te hoog.
Het aantal mensen dat psychische hulp nodig heeft blijft stijgen en het
psychisch welbevinden in de maatschappij neemt af.[8 ] Tegelijkertijd heeft de
sector te kampen met grote personele schaarste.[9 ] Al deze zaken hebben als
gevolg dat de toegankelijkheid van de ggz onder druk staat en de ggz al
langer te maken heeft met (te) hoge wachttijden. Om te komen tot een
betaalbare, kwalitatief goede én toegankelijke ggz voor iedereen die haar
nodig heeft is een brede aanpak nodig.

6 Kamerstuk 25 424, nr. 650 (25 424, nr. 650).
7 NZa, 31 augustus 2023, «Zorgvraagtypering van belang voor terugdringen wachttijden»
Zorgvraagtypering van belang voor terugdringen wachttijden | Nieuwsbericht | Nederlandse
Zorgautoriteit (nza.nl).

8 Zie AF2059-Ggz-uit-de-knel.pdf (trimbos.nl)en het NEMESIS-3 onderzoek (2023) inzake
psychische aandoeningen in de algemene bevolking.

9 Zie de onderzoekscijfers binnen het programma Arbeidsmarkt Zorg en Welzijn van het CBS.


-----

programma Mentaal welzijn van ons allemaal en het programma Toekomstbestendige Arbeidsmarkt Zorg & Welzijn (TAZ)[10].

Vraag 8
Kunt u stap voor stap uitleggen hoe de data van de HoNOs+ vragenlijsten
bijdragen aan het terugdringen van de wachttijden in de ggz?

Antwoord 8
HoNOs+ vragenlijsten (Health of the Nations Outcome Scale) dragen indirect
bij aan het terugdringen van de wachttijden in de ggz. HoNOs+ vragenlijsten
dragen dus ook indirect bij aan het vergroten van de toegankelijkheid van de
ggz. Met behulp van de HoNOs+ vragenlijsten, een instrument afkomstig uit
Engeland, wordt uiteindelijk het proces van contractering ondersteund door
de mismatch tussen vraag en aanbod van zorg te verkleinen. Ik zal hieronder
toelichten hoe dit met elkaar samenhangt.
Zoals bij vraag 7 aangegeven kent de ggz (te) hoge wachttijden. Daarbij zijn
de wachttijden voor patiënten met ernstige of complexe problemen het
langst. Een van de verklaringen voor dit probleem is de mismatch tussen
vraag en aanbod van zorg. Dit wordt in de hand gewerkt doordat zorgaanbieders en zorgverzekeraars nu geen (gestandaardiseerde) informatie uit kunnen
wisselen over de ernst van de problematiek van een patiënt. Als zorgverzekeraar en zorgaanbieder geen «gestandaardiseerde taal» hebben om aan te
wijzen welke groepen patiënten een complexe zorgvraag hebben, dan is het
onduidelijk wat het aanbod en de vraag van zorg zou moeten zijn. Hierdoor is
het dus ook niet mogelijk specifieke afspraken te maken over het terugdringen van de wachttijd voor die groepen.
Om dit probleem van het ontbreken van een «gestandaardiseerde taal» op te
lossen is zorgvraagtypering ontwikkeld. Zorgvraagtypering moet duidelijk
maken welke groep ggz-cliënten veel zorg nodig heeft, maar ook bij welke
groep cliënten een lagere zorgintensiteit te verwachten is. Om het systeem
achter de zorgvraagtypering nu verder te ontwikkelen en te verfijnen naar de
Nederlandse situatie in de praktijk, vraagt de NZa eenmalig de gegevens op
van de HoNOs+ vragenlijst die behandelaren invullen voor of tijdens de
behandeling. Met behulp van dit verbeterde systeem achter de zorgvraagtypering op basis van de HoNOs+ vragenlijsten, wordt inzichtelijker op basis
van objectieve criteria bij welke zorgaanbieders patiënten met een complexe
zorgvraag worden behandeld. Vervolgens kunnen zorgaanbieders en
zorgverzekeraars in het kader van het contracteringsproces overleggen over
inkoop van voldoende zorg en passende vergoedingen voor de behandeling
van de patiëntengroepen met een zwaardere zorgvraag. Op deze wijze dragen
HoNOs+ vragenlijsten indirect bij aan het verminderen van de wachttijden.
In het licht van bovenstaand proces hecht ik er waarde aan om nogmaals te
benadrukken dat de Autoriteit Persoonsgegevens (AP) eerder heeft geconstateerd dat de NZa de geschiktheid van verwerking van de HoNOs+ gegevens
van ggz-patiënten ten behoeve van het verbeteren van de zorgvraagtypering
aannemelijk heeft gemaakt.[11 ]

Vraag 9
Bent u bereid om deze vragen alle afzonderlijk te beantwoorden?

Antwoord 9
Ja, ik ben bereid om dat te doen.

10 Zie Integraal Zorgakkoord: «Samen werken aan gezonde zorg» | Rapport | Rijksoverheid.nl,
GALA -Gezond en Actief Leven Akkoord | Rapport | Rijksoverheid.nl, Aanpak Mentale
gezondheid van ons allemaal | Rapport | Rijksoverheid.nl & Programma Toekomstbestendige
Arbeidsmarkt Zorg en Welzijn | Rapport | Rijksoverheid.nl.

11 3628105–1050416-CZ.


-----

"""
	
	def test_split_sinuglar_qa(self):
		pre = Preprocessor()
		doc="""\n\nVraag 1
Wat is de hoofdstad van Nederland? 
\nAntwoord 1
Amsterdam"""
		print(pre.get_question_and_answer(doc))
		self.assertEqual(pre.get_question_and_answer(doc), [['Vraag 1\nWat is de hoofdstad van Nederland?'], ['Antwoord 1\nAmsterdam']])
	def test_split_multiple_qa(self):
		pre = Preprocessor()
		doc = """\n\nVraag 1
Wat is de hoofdstad van Nederland?
\nAntwoord 1
Amsterdam 
\nVraag 2
Wat is de hoofdstad van België?
\nAntwoord 2
Brussel"""
		self.assertEqual(pre.get_question_and_answer(doc), [['Vraag 1\nWat is de hoofdstad van Nederland?', 'Vraag 2\nWat is de hoofdstad van België?'], ['Antwoord 1\nAmsterdam', 'Antwoord 2\nBrussel']])
	def	test_split_page_qa(self):
		pre = Preprocessor()
		doc = """\n\nVraag 1
Wat is de hoofdstad van Nederland? 
\nAntwoord 1
Amsterdam
\nVraag 2
Wat is de hoofdstad van België?
\nAntwoord 2
Brussel
\nVraag 3
Wat is de hoofdstad van Frankrijk?
\nAntwoord 3
Parijs"""
		self.assertEqual(pre.get_question_and_answer(doc), [['Vraag 1\nWat is de hoofdstad van Nederland?', 'Vraag 2\nWat is de hoofdstad van België?', 'Vraag 3\nWat is de hoofdstad van Frankrijk?'], ['Antwoord 1\nAmsterdam', 'Antwoord 2\nBrussel', 'Antwoord 3\nParijs']])
	def test_split_doc_one_qa(self):
		pre = Preprocessor()
		doc = self.whole_doc
		expected_output = [['Vraag 1\nBent u bekend met de recente berichtgeving omtrent Nagorno-Karabach, in\nhet bijzonder de commentaren «Netjes gezuiverd»[1 ] en «Goede bedoelingen\nvan de EU zijn weinig waard als de harde machtsverhoudingen verschuiven»[2]?', 'Vraag 2\nIn hoeverre kan er worden gesproken van een etnische zuivering in NagornoKarabach? Deelt u de opvatting dat Nagorno-Karabach weliswaar niet met\ngeweld etnisch wordt gezuiverd, maar dat de oorspronkelijke bewoners van\nhet gebied vanwege de serieuze geweldsdreigingen, de uithongeringstactieken en de bedreigende taal van de Azerbeidzjaanse president Alijev geen\nandere keuze hebben dan te vertrekken en dat er in die zin weldegelijk sprake\nis van een etnische zuivering? En wat betekent deze constatering voor het\nhandelingskader van de Europese Unie (EU) jegens Azerbeidzjan?', 'Vraag 3\nKlopt het dat u recent met de Hoge vertegenwoordiger van de Unie voor\nbuitenlandse zaken en veiligheidsbeleid heeft gesproken over de situatie in\nNagorno-Karabach? Zo ja, kunt u schetsen wat de komende periode de\nEuropese inzet wordt richting Azerbeidzjan? Worden er sancties ingesteld\ntegen degenen die de gedwongen exodus hebben vormgegeven?', 'Vraag 4 en 5\nDeelt u de zorg dat Azerbeidzjan mogelijk op korte termijn militair een\ndoorgang zal proberen te forceren naar de Azerbeidjaanse exclave\nNachitsjevan, hetgeen een grove schending van het internationaal recht zou\nbetekenen?\nHoe wordt door de Europese Unie geanticipeerd op deze mogelijke\ngeweldsescalatie? Welke maatregelen worden voorbereid indien Azerbeidzjan\nbesluit Armenië binnen te vallen?', 'Vraag 6\nKunt u uiteenzetten in welke mate de Europese Unie afhankelijk is van\nAzerbeidjaans gas en hoe deze afhankelijkheid er de komende jaren uit gaat\nzien indien er geen koerswijziging plaatsvindt?', 'Vraag 7\nWordt er naar aanleiding van de recente gebeurtenissen in Azerbeidzjan al\nactief gezocht naar vervanging van Azerbeidjaans gas? Zo nee, waarom niet,\nen kunt u dit als voorstel op tafel leggen tijdens de eerstvolgende Raad\nBuitenlandse Zaken?', 'Vraag 8\nWelke maatregelen heeft de Europese Unie inmiddels getroffen tegen\ndoorvoerland Azerbeidzjan naar aanleiding van het 11e sanctiepakket?', 'Vraag 9\nWelke noodhulp verlenen Nederland en de Europese Unie aan Armenië maar\naanleiding van de recente gebeurtenissen en welke mogelijkheden ziet u om\ndit verder op te schalen?', 'Vraag 10\nKunt u in de beantwoording van deze vragen ook ingaan op de voortgang die\nwordt geleverd naar aanleiding van de motie van de leden Bikker en Omtzigt\n(Kamerstuk 36 410, nr. 74)?'], ['Antwoord 1\nJa.', 'Antwoord 2\nHet leidt geen twijfel dat de etnisch Armeense bewoners van NagornoKarabach het gebied zijn ontvlucht omdat zij zich niet veilig voelden, o.a.\nvanwege de maandenlange blokkade van de Lachin-corridor. Of er gesproken\nkan worden van een etnische zuivering is een juridisch ingewikkelde kwestie.\nHet kabinet zal in een separate brief op deze vraag ingaan, mede in het kader\nvan de aangenomen motie van het Lid Ceder over op basis van feiten', 'Antwoord 3\nHet klopt dat ik hierover, op 27 september jl., met de Hoge Vertegenwoordiger heb gesproken. Daarnaast is tijdens de Raad Buitenlandse Zaken (RBZ)\nvan 23 oktober jl. ook kort gesproken over deze situatie.\nHV Borrell stelde tijdens de RBZ ten aanzien van steun voor Armenië voor dat\nEDEO de mogelijkheden voor non-lethale steun onder de Europese Vredesfaciliteit (EPF) zorgvuldig zal verkennen. Hetzelfde geldt voor de mogelijkheden\nom de Europese Unie Missie in Armenië (EUMA) te versterken met meer\nmensen en meer patrouilles. EDEO zal voorts, met een missie naar Armenië,\nde mogelijkheden voor economische steun in kaart brengen. Nederland heeft\nconform de motie van het lid Ceder[4 ] in de Raad steun uitgesproken voor\nbovenstaande ideeën en andere EU-lidstaten opgeroepen dit ook te doen.\nTevens heeft Nederland conform de motie van leden Bikker en Omtzigt\naangegeven dat in geval van nieuw geweld binnen de EU gesproken moet\nworden over gepaste maatregelen.[5 ] De HV gaf aan dat de Armeense Minister\nvan Buitenlandse Zaken uitgenodigd zal worden voor de RBZ van november.', 'Antwoord 4 en 5\nIn het trilaterale akkoord van 2020 is expliciet vermeld dat alle economische\nen transportverbindingen van en naar Nachitsjevan gedeblokkeerd worden,\nwelke onbelemmerd verkeer van personen, voertuigen en vracht in beide\nrichtingen zou bewerkstelligen.\nHet kabinet heeft momenteel geen aanwijzingen dat Azerbeidzjan plannen\nheeft om een doorgang te forceren naar de exclave Nachitsjevan.\nAzerbeidzjan heeft publiekelijk bevestigd dat het de route naar Nachitsjevan\nmet en via Iran verder wil ontwikkelen. Nederland en de EU blijven inzetten\nop het zo snel mogelijk hervatten van de vredesonderhandelingen tussen\nArmenië en Azerbeidzjan, ook om wederzijdse erkenning van de Armeense en\nAzerbeidzjaanse territoriale integriteit expliciet vast te leggen. Wat betreft\nmaatregelen in geval van nieuw geweld zij verwezen naar mijn interventie\ntijdens de RBZ van 23 oktober jl., zie ook het antwoord op vraag 3.', 'Antwoord 6\nIn juli 2022 heeft de voorzitter van de Europese Commissie Ursula Von der\nLeyen een memorandum van overeenstemming getekend met Azerbeidzjan\nom de gasexport naar de EU te verdubbelen. Dit is in lijn met de EU-inzet', 'Antwoord 7\nDe EU beraadt zich momenteel allereerst op de wijze waarop Armenië\ngesteund kan worden. Hierover is kort gesproken tijdens de Raad Buitenlandse Zaken (RBZ) van 23 oktober jl. Zoals vermeld in het verslag van de\nRBZ stelde de Hoge Vertegenwoordiger Borrell in dit kader voor dat EDEO de\nmogelijkheden voor non-lethale EPF zorgvuldig zal verkennen. Hetzelfde geldt\nvoor de mogelijkheden om de Europese Unie Missie in Armenië (EUMA) te\nversterken met meer mensen en meer patrouilles. EDEO zal voorts, met een\nmissie naar Armenië, de mogelijkheden voor economische steun in kaart\nbrengen. Nederland heeft conform de motie van het lid Ceder[7 ] in de Raad\nsteun uitgesproken voor bovenstaande ideeën en andere EU-lidstaten\nopgeroepen dit ook te doen. Tevens heeft Nederland conform de motie van\nleden Bikker en Omtzigt aangegeven dat in geval van nieuw geweld binnen\nde EU gesproken moet worden over gepaste maatregelen[8].', 'Antwoord 8\nAzerbeidzjan heeft de aandacht van de EU en Nederland als het gaat om\nomzeiling. Op dit moment is er geen concrete aanleiding voor specifieke\nmaatregelen ten aanzien van Azerbeidzjan. In algemene zin geldt dat met het\n11[e ] sanctiepakket een belangrijk signaal is gegeven dat de EU de omzeiling\nvan sancties stevig aanpakt. Er zijn exportbeperkingen opgelegd tegen\nbedrijven uit VAE, Oezbekistan en Hongkong wegens betrokkenheid bij\nomzeiling.\nOok is er een stappenplan opgenomen voor de aanpak van omzeiling,\nbestaande uit (1) het intensiveren van samenwerking met derde landen door\ndiplomatieke outreach, (2) passende individuele maatregelen tegen marktdeelnemers uit derde landen betrokken bij het faciliteren van omzeiling en\n(3) in het uiterste geval de mogelijkheid tot opleggen exportrestricties voor\neen land als geheel. Besluitvorming hierover geschiedt met unanimiteit,\nvoorafgegaan door grondige analyse, inclusief reeds ondernomen acties en\nvoorwaarde dat het land in kwestie is geïnformeerd en geconsulteerd.\nNederland steunt EU-sanctiegezant O’Sullivan in zijn diplomatieke inspanningen gericht op derde landen waar omzeiling plaatsvindt en met analyses die\nbijdragen aan het bovengenoemde stappenplan.', 'Antwoord 9\nIn de brief op verzoek van uw Kamer d.d. 11 oktober 2023 (Kamerstuk\n21 501-02, nr. 2737) gaat het kabinet nader in op de internationale hulpverlening en de Nederlandse bijdrage daaraan in Nagorno-Karabach en in\nArmenië. Het kabinet heeft zich in internationaal verband ingezet voor\nonbelemmerde humanitaire toegang tot Nagorno-Karabach. Ook stelt het', 'Antwoord 10\nHet kabinet heeft, conform motie Bikker/Omtzigt (Kamerstuk 36 410, nr. 74), in\nEU-kader erop aangedrongen maatregelen tegen Azerbeidzjan te bespreken.\nTijdens de Raad Buitenlandse Zaken (RBZ) van 23 oktober jl. heeft Nederland\naangegeven dat in geval van nieuw geweld binnen de EU gesproken moet\nworden over gepaste maatregelen[9].']]
		print(pre.get_question_and_answer(doc))
		self.assertEqual(pre.get_question_and_answer(doc), expected_output)
	def test_split_doc_two_qa(self):
		pre = Preprocessor()
		doc = self.whole_doc2
		expected_output = [['Vraag 1\nWat is uw reactie op de uitslag van de peiling van MIND dat 74% van de\nrespondenten niet via de hulpverlener geïnformeerd is over het feit dat\ngegevens worden doorgegeven en dat 72% van de respondenten niet is\ngewezen op de mogelijkheid om een zogeheten privacyverklaring in te\nvullen?[1 ]', 'Vraag 3\nKlopt het dat bij het ondertekenen van de eerdergenoemde privacyverklaring\nniet alleen het delen van de gegevens met de NZa wordt stopgezet, maar ook\nhet delen van gegevens met de desbetreffende zorgverzekeraar? Waarom is\ner destijds geen aparte privacyverklaring ontwikkeld die alleen over het delen\nvan gegevens met de NZa gaat?', 'Vraag 4\nZijn er gevallen bekend waarbij gegevens van ggz-cliënten die een privacyverklaring hadden ondertekend alsnog doorgegeven zijn door de ggzinstelling aan de NZa? Zo ja, om hoeveel gevallen gaat het?', 'Vraag 5\nWelke procedure treedt er bij de NZa in werking als blijkt dat een ggzinstelling onterecht gegevens heeft doorgegeven van cliënten die een\nprivacyverklaring hadden ondertekend?', 'Vraag 6\nHoe komt het dat in uw brief van 13 april 2023 over het zorgprestatiemodel\nen de zorgvraagtypering[6 ] het argument van het terugdringen van de\nwachttijden in de ggz niet genoemd werd, terwijl dit nu wel als belangrijkste\nargument wordt gebruikt door de NZa voor de data-uitvraag voor de\nzorgvraagtypering?[7 ]', 'Vraag 7\nWat zijn volgens u de oorzaken van de lange wachttijden in de ggz?', 'Vraag 8\nKunt u stap voor stap uitleggen hoe de data van de HoNOs+ vragenlijsten\nbijdragen aan het terugdringen van de wachttijden in de ggz?', 'Vraag 9\nBent u bereid om deze vragen alle afzonderlijk te beantwoorden?'], ['Antwoord 1\nIk vind dit onwenselijk. Ik verwacht van zorgaanbieders dat zij hun cliënten en\npatiënten over de privacyverklaring goed, volledig en neutraal informeren, de\nkeuze altijd helemaal bij de patiënt laten en daar geen invloed op uitoefenen.\nDe Nederlandse Zorgautoriteit (NZa) heeft ter ondersteuning ook een\ninformatiefolder opgesteld om cliënten en patiënten te informeren.[2 ] De NZa\nheeft bij mij aangegeven deze patiëntenfolder actief te delen met zorgaanbieders, zodat zij cliënten en patiënten op hun beurt kunnen informeren. Naar\naanleiding van berichtgeving in verschillende media over privacy in het licht\nvan de data-uitvraag van de NZa voor de zorgvraagtypering heeft de NZa ook\nextra aandacht besteed aan privacy in de geestelijke gezondheidszorg (ggz)\nvia hun website.[3 ] Dit alles om cliënten en patiënten zo goed mogelijk te\ninformeren en in staat te stellen om de keuze te maken of zij willen dat hun\ngegevens met de NZa worden gedeeld.', 'Antwoord 2\nDe NZa geeft bij mij aan dat gegevensdeling in de zorg niet nieuw is. Daarom\ngaat de NZa er van uit dat zorgaanbieders de uitvraag rond zorgvraagtypering onderdeel hebben gemaakt van het gesprek dat zij voeren over\ngegevensdeling met cliënten en patiënten. De NZa heeft mij laten weten dat\nde hier bedoelde privacyverklaring ook al sinds 2014 bestaat en er daarom\nvanuit gaat dat zorgverleners bekend zijn met deze privacyverklaring. Zoals\nbij het antwoord op vraag 1 aangegeven verwacht ik daarbij dat zorgaanbieders hun patiënten zo goed mogelijk, neutraal en in begrijpelijke taal\ninformeren over de privacyverklaring en het verzamelen van hun zorg- en\nbehandelgegevens door de NZa, zodat deze zelf een beslissing kunnen\nnemen over het delen van hun gegevens met de NZa door hun zorgverlener.', 'Antwoord 3\nHet klopt dat de privacyverklaring geldt voor verzending van gegevens aan\nzowel zorgverzekeraars als aan de NZa. De NZa heeft mij laten weten in 2021\nen 2022 onderzocht te hebben of het mogelijk was de privacyverklaring op te\nsplitsen, zodat kon worden aangegeven welke partij of welke set gegevens\nniet mogen inzien. Gegevensdeling is echter zeer afhankelijk van de\nICT-infrastructuur bij zorgaanbieders. De partijen die de ICT-systemen van\nzorgaanbieders verzorgen gaven in dit kader aan de NZa aan dat het\nonmogelijk was deze splitsing (tijdig) gerealiseerd te krijgen.', 'Antwoord 4\nHet aanleveren van de medisch-inhoudelijke gegevens wanneer een patiënt\neen privacyverklaring heeft ondertekend is expliciet uitgesloten in de\nRegeling ggz en fz en in de aanleverstandaard zorgvraagtypering.[4 5 ] De NZa\ngeeft bij mij aan de eigen systemen zo georganiseerd te hebben dat het\nonmogelijk is de uitgesloten gegevens van een patiënt te ontvangen wanneer\nin de aanlevering is aangegeven dat er sprake is van een privacyverklaring.\nUit een recente test blijkt dan ook dat er geen medisch-inhoudelijke gegevens\naanwezig zijn voor patiënten bij wie is aangegeven dat zij een privacyverklaring hebben ondertekend.\nEerder is wel gebleken dat één ICT-systeem niet in alle gevallen aangaf dat er\neen privacyverklaring was ondertekend door een probleem in de programmatuur van dat ICT-systeem. Zodra de NZa hier een signaal over ontving is zij in\noverleg getreden met de ICT-leverancier en heeft verzocht bij haar klanten, de\nzorgaanbieders, na te gaan of het probleem zich bij hen had voorgedaan. De\nNZa heeft bij mij aangegeven van in totaal vijf zorgaanbieders het signaal te\nhebben ontvangen dat dit probleem zich ook bij hen heeft voorgedaan. De\nNZa heeft vervolgens de bestanden waarin deze fout zat verwijderd en heeft', 'Antwoord 5\nDe NZa geeft bij mij aan géén gegevens te willen verwerken die zij niet mag\nverwerken. Om die reden wordt de aanlevering van de gegevens van\npatiënten waarbij bekend is dat dat ze privacyverklaring hebben ondertekend\nautomatisch afgewezen en verwijderd, zoals ook aangegeven in antwoord op\nvraag 4. De zorgaanbieder ontvangt hiervan bericht met het verzoek de\ngegevens aan te passen en opnieuw aan te leveren.\nAls het voorkomt dat de automatische veiligheidsmechanismen niet in\nwerking treden, omdat in het bestand van de zorgaanbieder niet wordt\naangegeven dat er sprake is van een privacyverklaring terwijl dat wel het\ngeval is, neemt de NZa direct contact op met de betreffende ICT-leverancier.\nDe NZa verwijdert deze bestanden en verzoekt de gegevens opnieuw aan te\nleveren zonder de gegevens van patiënten die een privacyverklaring hebben\nondertekend, zoals ook bij vraag 4 toegelicht. De NZa heeft onderzoek gedaan\nof dit soort situaties met extra automatische of menselijke interventies\nvoorkomen kunnen worden. Dit blijkt helaas niet het geval volgens de NZa,\nomdat de fout zit in de ICT-systemen waaruit de bestanden worden aangeleverd.', 'Antwoord 6\nIn de brief van 13 april 2023 bent u geïnformeerd over de uitkomsten van de\neerste evaluatie van het zorgprestatiemodel, hierin heb ik expliciet stilgestaan\nbij de toegankelijkheid van de ggz: «Dit [het zorgprestatiemodel] draagt bij\n_aan een goede ggz, die toegankelijk is voor iedereen die haar nodig heeft.»_\nEen goede ggz die toegankelijk is, is voor mij een ggz die de wachttijden\nweet terug te dringen en zo mensen tijdig en goed zorg kan bieden. Ik heb in\ndeze brief, zij het in iets andere bewoordingen, dus weldegelijk het argument\nvan terugdringen van wachttijden aangehaald als belangrijke reden voor\ninvoering van zorgprestatiemodel en de daarmee samenhangende dataverzameling.', 'Antwoord 7\nHiervoor zijn meerdere redenen. De druk op de ggz is al langere tijd te hoog.\nHet aantal mensen dat psychische hulp nodig heeft blijft stijgen en het\npsychisch welbevinden in de maatschappij neemt af.[8 ] Tegelijkertijd heeft de\nsector te kampen met grote personele schaarste.[9 ] Al deze zaken hebben als\ngevolg dat de toegankelijkheid van de ggz onder druk staat en de ggz al\nlanger te maken heeft met (te) hoge wachttijden. Om te komen tot een\nbetaalbare, kwalitatief goede én toegankelijke ggz voor iedereen die haar\nnodig heeft is een brede aanpak nodig.', 'Antwoord 8\nHoNOs+ vragenlijsten (Health of the Nations Outcome Scale) dragen indirect\nbij aan het terugdringen van de wachttijden in de ggz. HoNOs+ vragenlijsten\ndragen dus ook indirect bij aan het vergroten van de toegankelijkheid van de\nggz. Met behulp van de HoNOs+ vragenlijsten, een instrument afkomstig uit\nEngeland, wordt uiteindelijk het proces van contractering ondersteund door\nde mismatch tussen vraag en aanbod van zorg te verkleinen. Ik zal hieronder\ntoelichten hoe dit met elkaar samenhangt.\nZoals bij vraag 7 aangegeven kent de ggz (te) hoge wachttijden. Daarbij zijn\nde wachttijden voor patiënten met ernstige of complexe problemen het\nlangst. Een van de verklaringen voor dit probleem is de mismatch tussen\nvraag en aanbod van zorg. Dit wordt in de hand gewerkt doordat zorgaanbieders en zorgverzekeraars nu geen (gestandaardiseerde) informatie uit kunnen\nwisselen over de ernst van de problematiek van een patiënt. Als zorgverzekeraar en zorgaanbieder geen «gestandaardiseerde taal» hebben om aan te\nwijzen welke groepen patiënten een complexe zorgvraag hebben, dan is het\nonduidelijk wat het aanbod en de vraag van zorg zou moeten zijn. Hierdoor is\nhet dus ook niet mogelijk specifieke afspraken te maken over het terugdringen van de wachttijd voor die groepen.\nOm dit probleem van het ontbreken van een «gestandaardiseerde taal» op te\nlossen is zorgvraagtypering ontwikkeld. Zorgvraagtypering moet duidelijk\nmaken welke groep ggz-cliënten veel zorg nodig heeft, maar ook bij welke\ngroep cliënten een lagere zorgintensiteit te verwachten is. Om het systeem\nachter de zorgvraagtypering nu verder te ontwikkelen en te verfijnen naar de\nNederlandse situatie in de praktijk, vraagt de NZa eenmalig de gegevens op\nvan de HoNOs+ vragenlijst die behandelaren invullen voor of tijdens de\nbehandeling. Met behulp van dit verbeterde systeem achter de zorgvraagtypering op basis van de HoNOs+ vragenlijsten, wordt inzichtelijker op basis\nvan objectieve criteria bij welke zorgaanbieders patiënten met een complexe\nzorgvraag worden behandeld. Vervolgens kunnen zorgaanbieders en\nzorgverzekeraars in het kader van het contracteringsproces overleggen over\ninkoop van voldoende zorg en passende vergoedingen voor de behandeling\nvan de patiëntengroepen met een zwaardere zorgvraag. Op deze wijze dragen\nHoNOs+ vragenlijsten indirect bij aan het verminderen van de wachttijden.\nIn het licht van bovenstaand proces hecht ik er waarde aan om nogmaals te\nbenadrukken dat de Autoriteit Persoonsgegevens (AP) eerder heeft geconstateerd dat de NZa de geschiktheid van verwerking van de HoNOs+ gegevens\nvan ggz-patiënten ten behoeve van het verbeteren van de zorgvraagtypering\naannemelijk heeft gemaakt.[11 ]', 'Antwoord 9\nJa, ik ben bereid om dat te doen.']]
		self.assertEqual(pre.get_question_and_answer(doc), expected_output)
	def test_split_empty_qa(self):
		pre = Preprocessor()
		doc = ""
		expected_output = [[],[]]
		self.assertEqual(pre.get_question_and_answer(doc), expected_output)
	def test_split_lorum_ipsum_qa(self):
		pre = Preprocessor()
		doc = "Lorum ipsum dolor sit amet, consectetur adipiscing elit. Nullam nec pur"
		expected_output = [[],[]]
		self.assertEqual(pre.get_question_and_answer(doc), expected_output)
	def test_get_context_doc_one(self):
		pre = Preprocessor()
		self.assertEqual("""Vergaderjaar 2023–2024 Aanhangsel van de Handelingen

Vragen gesteld door de leden der Kamer, met de daarop door de
regering gegeven antwoorden

Vragen van het lid Boswijk (CDA) aan de Minister van Buitenlandse Zaken
over de situatie in de Zuidelijke Kaukasus (ingezonden 2 oktober 2023).

Antwoord van Minister Bruins Slot (Buitenlandse Zaken) (ontvangen
13 november 2023)."""
,pre.get_heading(self.whole_doc))

	def test_get_context_doc_two(self):
		pre = Preprocessor()
		self.assertEqual("""Vergaderjaar 2023–2024 Aanhangsel van de Handelingen

Vragen gesteld door de leden der Kamer, met de daarop door de
regering gegeven antwoorden

Vragen van het lid Dijk (SP) aan de Minister voor Langdurige Zorg en Sport
over antwoord op de vragen inzake de uitzending «Het geheim van de
_spreekkamer» en het artikel «Zorgverzekeraars hebben groot belang bij de data_
_die toezichthouder verzamelt» en Peiling MIND: meerderheid cliënten niet_
_geïnformeerd over gegevensdeling met de NZa (ingezonden 3 oktober 2023)._

Antwoord van Minister Helder (Langdurige Zorg en Sport) (ontvangen
24 oktober 2023).""", pre.get_heading(self.whole_doc2))

	def test_get_footnotes_doc_one(self):
		pre = Preprocessor()
		result = pre.get_footnotes(self.whole_doc)
		self.assertEqual(result, ['1 Nederlands Dagblad, 29 september 2023, «De ondergang van Nagorno Karabach is verbonden', '2 De Volkskrant, 20 september 2023, «Goede bedoelingen van de EU zijn weinig waard als de', '3 Kamerstuk 21 501-02, nr. 2733', '4 Motie Ceder, Kamerstuk 21 501-02, nr. 2732', '5 Motie Bikker en Omtzigt, Kamerstuk 36 410, nr. 31', '6 Gegevens ENTSOG, Enerdata.net', '7 Motie Ceder, Kamerstuk 21 501-02 nr. 2732', '8 Motie Bikker en Omtzigt, Kamerstuk 36 410, nr. 31', '9 Motie Bikker en Omtzigt, Kamerstuk 36 410, nr. 31'])
	def test_get_footnotes_doc_two(self):
		pre = Preprocessor()
		result = pre.get_footnotes(self.whole_doc2)
		self.assertEqual(result, ['1 Aanhangsel van de Handelingen, vergaderjaar 2023–2024, nr. 76 (2023D39037); Mind Platform,', '2 https://puc.overheid.nl/nza/doc/PUC_743104_22/1/.', '3 Privacy in de ggz | Geestelijke gezondheidszorg (ggz) en forensische zorg (fz) | Nederlandse', '4 Standaard voor gegevensaanlevering zorgvraagtypering (ggz & fz) – versie 1.3 – Nederlandse', '5 Regeling geestelijke gezondheidszorg en forensische zorg – NR/REG-2313a – Nederlandse', '6 Kamerstuk 25 424, nr. 650 (25 424, nr. 650).', '7 NZa, 31 augustus 2023, «Zorgvraagtypering van belang voor terugdringen wachttijden»', '8 Zie AF2059-Ggz-uit-de-knel.pdf (trimbos.nl)en het NEMESIS-3 onderzoek (2023) inzake', '9 Zie de onderzoekscijfers binnen het programma Arbeidsmarkt Zorg en Welzijn van het CBS.', '10 Zie Integraal Zorgakkoord: «Samen werken aan gezonde zorg» | Rapport | Rijksoverheid.nl,', '11 3628105–1050416-CZ.'])


if __name__ == '__main__':
		unittest.main()
