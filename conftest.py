import pytest
from selenium import webdriver
from pages.login.login_page import LoginPage
from tools.mongodb import check_mongodb_connection, mongodb_last_user
from tools.postgresql import check_pg_connection, activate_setup_trial_modal

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


@pytest.fixture(scope='session', autouse=True)
def mongodb_check():
    check_mongodb_connection()


@pytest.fixture()
def activating_setup_trial_modal():
    activate_setup_trial_modal(mongodb_last_user(data='user_name'))


@pytest.fixture(scope='module')
def login_in(driver):
    login = LoginPage(driver)
    login.login_in()



