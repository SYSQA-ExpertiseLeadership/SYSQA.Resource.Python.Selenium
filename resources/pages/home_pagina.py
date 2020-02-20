'''
Een pagina is opgebouwd uit drie onderdelen.

Eerst de veelgebruikte flows: Dit zijn sets van handelingen die samen een doel bereiken.
Denk daarbij bijvoorbeeld aan inloggen: dit bestaat uit drie handelingen: Het invullen
van de gebruikersnaam, het invullen van het wachtwoord, en het klikken op de inlogknop.
Functies onder veelgebruikte flows verwijzen naar andere veelgebruikte flows en naar de
losse handelingen eronder.

De losse handelingen zijn functies die precies één handeling beschrijven. Zij verwijzen
weer terug naar de locators en naar functionaliteit in basepage.py. De Locators staan
onderaan.

Deze opbouw betekent dat als meerdere flows naar dezelfde handeling verwijzen, en die
handeling geüpdatet moet worden, dat op maar één plek geüpdatet moet worden en daarna
automatisch al je tests het weer doen. Hetzelfde geldt voor meerdere handelingen die
naar één element verwijzen - als de locator van dat element ooit verandert, hoef je
maar één plek te updaten.
'''

from selenium.webdriver.common.by import By

from resources import data
from resources import basepage as BP

#######################
# Veelgebruikte flows #
#######################

def gebruik_zoekbalk(zoekterm):
    '''Vul de zoekbalk in, en klik op zoeken'''

    vul_zoekbalk_in(zoekterm)
    click_zoeken()


#####################
# Losse handelingen #
#####################

def benader_home_pagina():
    '''Benadert de URL van mvnrepository'''
    BP.go_to_url(data.URL)


def vul_zoekbalk_in(waarde):
    '''Vult de zoekbalk in.'''
    BP.write(LOCATORS["Zoekbalk"], waarde)


def click_zoeken():
    '''Klik op 'Search'.'''
    BP.click(LOCATORS["Zoekknop"])

############
# Locators #
############

LOCATORS = {
    "Zoekbalk": (By.ID, "query"),
    "Zoekknop": (By.CSS_SELECTOR, "input[value='Search']")
}
