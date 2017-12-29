import pytest
from data.cms import cms_tutorial_link, cms_market_place
from pages.setup.setup_page import SetupPage
from pages.login.login_page import LoginPage
from tools.check_email import check_email
from tools.mongodb import mongodb_last_user
from pages.account_settings.account_settings_page import AccountSettings
from data.users import REAL_USER_EMAIL


def test_trial_modal(driver):
    setup = SetupPage(driver)
    login = LoginPage(driver)
    login.open_login_page()
    login.login_in(mongodb_last_user(), '123456')
    setup.click_sign_up_next_step_button()
    assert setup.is_popup_title()


def test_check_account_setting_link(driver):
    setup = SetupPage(driver)
    login = LoginPage(driver)
    settings = AccountSettings(driver)
    login.open_login_page()
    login.login_in(mongodb_last_user(), '123456')
    setup.open_setup_sign_up_page()
    setup.click_sign_up_settings_link()
    assert settings.is_save_changes_button()


def test_from_setup_to_integration(driver):
    setup = SetupPage(driver)
    login = LoginPage(driver)
    login.open_login_page()
    login.login_in(mongodb_last_user(), '123456')
    setup.open_setup_sign_up_page()
    setup.click_sign_up_next_step_button()
    assert setup.is_integration_api_url_label()


@pytest.mark.parametrize('cms_name,doc_link', cms_tutorial_link)
def test_check_cms_market(driver, cms_name, doc_link):
    setup = SetupPage(driver)
    login = LoginPage(driver)
    login.open_login_page()
    login.login_in(mongodb_last_user(), '123456')
    setup.open_setup_integration_page()
    setup.choose_cms(cms_name)
    setup.click_integration_watch_tutorial_link()
    assert setup.current_url() == doc_link


@pytest.mark.parametrize('cms_name,market_link', cms_market_place)
def test_check_cms_market(driver, cms_name, market_link):
    setup = SetupPage(driver)
    login = LoginPage(driver)
    login.open_login_page()
    login.login_in(mongodb_last_user(), '123456')
    setup.open_setup_integration_page()
    setup.choose_cms(cms_name)
    setup.click_integration_download_plugin_button()
    assert setup.current_url() == market_link


@pytest.mark.parametrize('cms_name,doc_link', cms_tutorial_link)
def test_send_instruction(driver, cms_name, doc_link):
    setup = SetupPage(driver)
    login = LoginPage(driver)
    login.open_login_page()
    login.login_in(mongodb_last_user(), '123456')
    setup.open_setup_integration_page()
    setup.choose_cms(cms_name)
    setup.click_integration_send_instruction_button()
    setup.enter_developer_email(REAL_USER_EMAIL)
    setup.click_integration_send_instruction_to_developer_button()
    setup.open_url(check_email('TriggMine integration instruction'))
    assert setup.current_url() == doc_link



