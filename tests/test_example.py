'''
In deze file plaatsen we onze testcases.
Probeer je testcases op een logische manier over verschillende bestanden te verdelen
(bijvoorbeeld alle tests voor één pagina bij elkaar). Ieder bestand moet met 'test_'
beginnen, anders vindt pytest ze niet.

Iedere test bestaat uit drie stappen:
ARRANGE, ACT en ASSERT

ARRANGE:
In deze stap doen we alle handelingen die nodig zijn om de test uit te kunnen voeren.
Denk hierbij aan het inloggen op de site, navigeren naar de pagina, of in de database
kijken wat het resultaat zou moeten zijn. Aan het einde van deze stap zijn we klaar om
de specefieke handeling uit te voeren die we willen testen.

ACT:
Nu alles klaar staat, gaan we de handeling doen die we willen testen. Hou deze stap zo
klein mogelijk. Hoe meer handelingen hier gedaan worden, hoe moeilijker het is te zeggen
waar de fout zit. Deze stap dient ook als documentatie voor jezelf en andere waar deze
testcase om draait. Test je het zoeken of het navigeren naar het zoeken?

ASSERT:
Hier vergelijk je de uitkomst met de gewenste uitkomst. Als het goed is hoef je hier
geen handelingen op de webpagina meer uit te voeren. Alleen de uitkomst ophalen en op
een logische manier vergelijken.

Ik vind het prettig om deze stappen als comments in de methode te zetten.
Hiermee geef je voor jezelf en je collegas aan wat de belangrijke delen zijn van de
testcase en wat slechts voorbereiding.

Ten slotte belangrijk: Python ondersteunt smileys in je comments! 😁
Niet nuttig, wel leuk.
'''

from resources.pages import home_pagina, result_pagina

def test_first_testcase():
    ''' Geeft geen foutmelding '''

    # Arrange
    home_pagina.benader_home_pagina()

    # Act
    home_pagina.gebruik_zoekbalk("selenium")

    # Assert
    assert result_pagina.tel_aantal_resultaten() == 774


def test_inconsistent_testcase():
    ''' Geeft wel een foutmelding '''

    # Arrange
    home_pagina.benader_home_pagina()

    # Act
    home_pagina.gebruik_zoekbalk("Test")

    # Assert
    assert result_pagina.tel_aantal_resultaten() == 1373
