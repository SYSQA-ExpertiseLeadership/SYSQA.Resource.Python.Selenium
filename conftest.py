'''
Deze code zorgt ervoor dat voor iedere test een browser opgestart wordt, en dat na iedere
test deze weer afgesloten wordt.
'''

import pytest

from resources.drivermanager import get_driver, close_driver

@pytest.fixture(autouse=True)
def driver_fixture():
    '''
    This fixture ensures a driver and browser exists at the start of a test, and that it
    closes afterwards
    '''
    get_driver()
    yield
    close_driver()
