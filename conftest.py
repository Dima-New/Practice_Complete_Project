import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# New option for terminal
def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en")


# Fixture for chrome driver setup with option, run and quit
@pytest.fixture(scope="function")
def driver(request):
    user_language = request.config.getoption("--language")
    options = Options()
    options.add_experimental_option("prefs", {"intl.accept_languages": user_language})
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    if request.cls is not None:  # check if tests in class or not
        request.cls.driver = driver
    yield driver
    driver.quit()
