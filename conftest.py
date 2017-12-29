import pytest
from selenium import webdriver
from data.cms import cms_tutorial_link
from tools.mongodb import check_mongodb_connection

browsers = {
    'chrome': webdriver.Chrome,
    # 'firefox': webdriver.Firefox,
    # 'ie': webdriver.Ie
}


@pytest.yield_fixture(scope="session", params=sorted(browsers.keys()))
def driver(request):
    browser = browsers[request.param]()
    yield browser
    browser.quit()


@pytest.fixture(autouse=True)
def mongodb_check():
    check_mongodb_connection()


