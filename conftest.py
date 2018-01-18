import pytest
import psycopg2
from selenium import webdriver
from pages.login.login_page import LoginPage
from tools.mongodb import check_mongodb_connection, mongodb_last_user
from tools.postgresql import activate_setup_trial_modal, set_support_email, set_logo_image

browsers = {
    'chrome': webdriver.Chrome,
    # 'firefox': webdriver.Firefox,
    # 'opera': webdriver.Opera
    # 'ie': webdriver.Ie
}


@pytest.yield_fixture(scope="session", params=sorted(browsers.keys()))
def driver(request):
    browser = browsers[request.param]()
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture(scope='module')
def login_in(driver):
    login = LoginPage(driver)
    login.login_in()


@pytest.fixture()
def activating_setup_trial_modal():
    activate_setup_trial_modal(mongodb_last_user(data='user_name'))


@pytest.fixture()
def add_support_email():
    set_support_email(mongodb_last_user(data='user_name'))


@pytest.fixture()
def add_logo_image():
    set_logo_image(mongodb_last_user(data='user_name'))


