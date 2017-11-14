import pytest
from selenium import webdriver
from Pages.Login.LoginPage import LoginPage
from Pages.Setup.SetupPage import SetupPage


browsers = {
    'chrome': webdriver.Chrome,
    # 'firefox': webdriver.Firefox
}


@pytest.yield_fixture(params=browsers.keys())
def driver(request):
    browser = browsers[request.param]()
    login_page = LoginPage(browser)
    login_page.open_page('https://client.triggmine.com.ua/login')
    yield login_page
    browser.quit()
