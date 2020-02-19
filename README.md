# SYSQA.Resource.Python.Selenium

## Doel

Met deze resource proberen we twee hoofddoelen te bereiken:

1. Het bieden van een beginproject om de opstartfase van een nieuw Seleniumproject te
    versnellen;
1. Het beschijven en uitleggen van één implementatie van het `Page-Object Model` om zo
    bij te dragen aan een overzichtelijk en onderhoudbaar Selenium Python project.

Om deze doelen te bereiken proberen we voor dit project een aantal uitgangspunten te
hanteren:

1. We blijven dicht bij de originele taal;
1. We houden het bij de basisfunctionaliteiten;
1. We zetten het zo op dat we eenvoudig kunnen uitbreiden en aanvullen;
1. We houden de setup- en ontwikkelomgeving zo eenvoudig mogelijk.

Je zult hopelijk snel merken dat je dingen wil doen die niet aan dit project zijn
toegevoegd. Wij hopen je genoeg kennis mee te hebben gegeven van de basis om deze dingen
zelf (of met onze hulp) aan je framework toe te kunnen voegen.

Dit doen we door de keuzes die we gemaakt hebben in dit project door middel van comments
en dit begeleidende document uit te leggen en mocht je meer willen weten (of aanvullingen
hebben), zoek dan voorall contact met ons.


## Belangrijk om te weten

Gedurende iedere stap in een project worden er keuzes gemaakt. Voor sommige dingen is het
belangrijk om vooraf te weten waarom bepaalde keuzes zijn gemaakt.

Dit is een kort overzicht van de redenatie achter een aantal belangrijke keuzes.


## Voorbereiding
De volgende stappen moet je nemen voor dat je aan dit project kunt beginnen.
* Installeer de benodigde software:
    * [Download en installeer Python 3](https://www.python.org/downloads/);
    * [Download en installeer Visual Studio Code](https://code.visualstudio.com/).
* Clone de gitrepository of [download de zip hier](https://github.com/SYSQA-ExpertiseLeadership/SYSQA.Resource.Python.Selenium-/archive/master.zip).
* Controleer of 'python' en 'pip' in je path staan:
    * Open een terminal (Windowstoets + R, type 'cmd', druk op ENTER);
    * Type 'python --version' en druk op Enter. Type 'pip --version' en druk op enter.
        Beiden zouden geen foutmelding moeten geven. Doen ze dit wel, google dan op
        'add python/pip to PATH';
* Start Visual Studio Code op, ga naar File -> Open Workspace, en selecteer de map waar
    je het project heb uitgepakt.
* Optioneel: Start hier een Virtual Environment. Als je niet weet wat het is, heb je het
    zeker weten niet nodig. Weet je wel wat het is, dan heb je het nog steeds
    waarschijnlijk niet nodig.
* Open een terminal in Visual Studio Code (Ctrl + Shift + `), en type
    'pip install -r requirements.txt'.
* Als het goed is, is in de verticale werkbalk links een nieuw symbool verschenen (een
    Erlenmeyerbeker), waarbij 'Test' verschijnt als je er met je muis overheen gaat. Klik
    hierop, en het tabblad 'TEST' verschijnt. Achter PYTHON verschijnen symbooltjes als
    je de muis erheen beweegt. Klik op de knop 'Discover Tests', en daarna op 'Run All
    Tests'.
* Onder OUTPUT verschijnt de testoutput, onder PROBLEMS de gefaalde tests en waarom ze gefaald zijn.

## Tips

## Bijdragen aan deze resource

### Tools 