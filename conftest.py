import pytest
from selenium import webdriver
from Pages.Login.LoginPage import LoginPage
from Pages.Setup.SetupPage import SetupPage


browsers = {
    'chrome': webdriver.Chrome,
    'firefox': webdriver.Firefox
}


@pytest.yield_fixture(params=browsers.keys())
def driver(request):
    browser = browsers[request.param]()
    # Тут я создаю ексзепляр класса и передаю ему драйвер.
    yield browser
    browser.quit()

@pytest.fixture()
def login(driver):
    login = LoginPage(driver)
    return login

@pytest.fixture()
def setup(driver):
    setup = SetupPage(driver)
    return setup