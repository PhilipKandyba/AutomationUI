import pytest
from selenium import webdriver
from Pages.Login.LoginPage import LoginPage


browsers = {
    'chrome': webdriver.Chrome,
    # 'firefox': webdriver.Firefox,
    # 'edge': webdriver.Edge
}


@pytest.yield_fixture(params=browsers.keys())
def driver(request):
    browser = browsers[request.param]()
    login_page = LoginPage(browser)
    yield login_page
    browser.quit()


@pytest.fixture()
def login(driver):
    login_page = LoginPage(driver)
    return login_page

