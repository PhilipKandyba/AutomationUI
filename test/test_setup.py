import pytest
from data.cms import cms
from pages.setup.setup_page import SetupPage
from pages.login.login_page import LoginPage
from tools.mongodb import mongodb_last_user
from pages.account_settings.account_settings_page import AccountSettings


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


@pytest.mark.parametrize('cms', cms)
def test_check_cms_market(driver):
    setup = SetupPage(driver)
    login = LoginPage(driver)
    login.open_login_page()
    login.login_in(mongodb_last_user(), '123456')
    setup.open_setup_integration_page()
    setup.choose_cms(cms)
