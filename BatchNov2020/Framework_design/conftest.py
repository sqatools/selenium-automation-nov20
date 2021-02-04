import pytest
from .features import  *

@pytest.fixture(scope="session")
def setup():
    launch_browser(url)
    yield
    driver.close()