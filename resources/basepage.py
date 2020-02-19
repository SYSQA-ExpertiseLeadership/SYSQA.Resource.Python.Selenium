'''
Base methods. Dit is de enige plek in je code waar je je driver aanspreekt. Mocht je
ooit van Selenium af willen stappen en je gehele project naar (bijvoorbeeld) Cypress
willen halen, is dit (en drivermanager.py) het enige wat geüpdatet moet worden. Andere
pagina's die je schrijft, importeren dit bestand.
'''

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from resources.drivermanager import get_driver

###################
# General Methods #
###################

def go_to_url(url):
    ''' Goes to an url. '''
    driver = get_driver()
    driver.get(url)

def find(locator):
    '''
    Waits until element, located by 'locator', is visible. Returns the element once found.
    '''
    driver = get_driver()
    wait = WebDriverWait(driver, 10)

    element = wait.until(EC.visibility_of_element_located(locator))
    return element

def read(locator):
    '''
    Waits until element, located by 'locator', is visible, then returns the text value.
    '''
    element = find(locator)
    return element.text

def click(locator):
    '''
    Waits until element, located by 'locator', is clickable. Clicks the element once found.
    '''
    driver = get_driver()
    wait = WebDriverWait(driver, 10)

    element = wait.until(EC.element_to_be_clickable(locator))
    element.click()

def write(locator, value):
    '''
    Waits until element, located by 'locator', is visible, then sends 'value'.
    '''
    element = find(locator)
    element.clear()
    element.send_keys(value)

############################
# Project Specific Methods #
############################
