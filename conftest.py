import pytest
from selenium import webdriver
from Data.URL import base_page_test
import requests

browsers = {
    'chrome': webdriver.Chrome,
    # 'firefox': webdriver.Firefox,
    # 'ie': webdriver.Ie
}


@pytest.yield_fixture(scope="module", params=sorted(browsers.keys()))
def driver(request):
    browser = browsers[request.param]()
    yield browser
    browser.quit()
