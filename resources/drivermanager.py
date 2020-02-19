'''
Deze pagina zorgt ervoor dat een driver aangemaakt wordt. De fixture in conftest.py roept
de functionaliteit 'get_driver()' en 'close_driver()' aan. '_create_driver()' begint met
een underscore ('_'), wat Pythons manier is om private functies aan te geven.

Door gebruik te maken van BrowserDriverManager, wordt automatisch een driver.exe
gedownload en geïnstalleerd bij het uitvoeren van de tests, als deze niet al aanwezig is.
'''

# pylint: disable=global-variable-undefined, invalid-name, global-statement

from selenium.webdriver import Chrome, Edge, Firefox, Opera
from webdrivermanager import ChromeDriverManager, EdgeDriverManager, GeckoDriverManager, \
                                OperaChromiumDriverManager

driver = None

def _create_driver(browser='Chrome'):
    '''
    Creates a driver
    '''
    global driver

    manager = {
        "Chrome"   : ChromeDriverManager(),
        "Edge"     : EdgeDriverManager(),
        "Firefox"  : GeckoDriverManager(),
        "Opera"    : OperaChromiumDriverManager()
    }
    drivers = {
        "Chrome"   : Chrome,
        "Edge"     : Edge,
        "Firefox"  : Firefox,
        "Opera"    : Opera
    }

    manager[browser].download_and_install()
    driver = drivers[browser]()

def close_driver():
    '''
    Closes driver
    '''
    global driver

    if "driver" in globals() and driver:
        driver.quit()
    driver = None

def get_driver():
    '''
    Returns a driver. If no driver is found, a new one is created first
    '''
    global driver

    if "driver" not in globals() or driver is None:
        _create_driver()
    return driver
