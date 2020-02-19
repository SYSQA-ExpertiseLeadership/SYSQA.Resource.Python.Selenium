'''
Result pagina. Het is een best practice om bovenaan iedere pagina een korte beschrijving
van de pagina te zetten. Visual Studio Code kan deze code laten zien wanneer je dit
bestand in andere scripts aanroept.
'''

from selenium.webdriver.common.by import By

from resources import basepage as BP

#######################
# Veelgebruikte flows #
#######################


#########################
# Losse functionaliteit #
#########################

def tel_aantal_resultaten():
    '''Benadert de URL van de inlogpagina voor behandelaars.'''
    aantal_string = BP.read(LOCATORS["Aantal resultaten"])
    aantal = int(aantal_string)
    return aantal

############
# Locators #
############

LOCATORS = {
    "Aantal resultaten": (By.CSS_SELECTOR, "#maincontent > h2 > b")
}
