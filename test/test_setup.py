import pytest
from data.cms import cms_tutorial_link, cms_market_place, cms_list
from pages.setup.setup_page import SetupPage
from pages.login.login_page import LoginPage
from tools.check_email import check_email
from pages.account_settings.account_settings_page import AccountSettings
from data.users import REAL_USER_EMAIL


# First entering to cabinet. Showing popup.
def test_trial_modal(driver):
    setup = SetupPage(driver)
    login = LoginPage(driver)
    login.open_login_page()
    login.login_in()
    setup.click_sign_up_next_step_button()
    assert setup.is_popup_title()


# Check "Account setting" link.
def test_check_account_setting_link(driver):
    setup = SetupPage(driver)
    login = LoginPage(driver)
    settings = AccountSettings(driver)
    login.open_login_page()
    login.login_in()
    setup.open_setup_sign_up_page()
    setup.click_sign_up_settings_link()
    assert settings.is_save_changes_button()


# Going from "Sign in" to "Integration"
def test_from_setup_to_integration(driver):
    setup = SetupPage(driver)
    login = LoginPage(driver)
    login.open_login_page()
    login.login_in()
    setup.open_setup_sign_up_page()
    setup.click_sign_up_next_step_button()
    assert setup.is_integration_api_url_label()


# Checking link of documentation for all plugins.
@pytest.mark.parametrize('cms_name,doc_link', cms_tutorial_link)
def test_check_cms_market(driver, cms_name, doc_link):
    setup = SetupPage(driver)
    login = LoginPage(driver)
    login.open_login_page()
    login.login_in()
    setup.open_setup_integration_page()
    setup.choose_cms(cms_name)
    setup.click_integration_watch_tutorial_link()
    assert setup.current_url() == doc_link


# Checking link of market place for all plugins.
@pytest.mark.parametrize('cms_name,market_link', cms_market_place)
def test_check_cms_market(driver, cms_name, market_link):
    setup = SetupPage(driver)
    login = LoginPage(driver)
    login.open_login_page()
    login.login_in()
    setup.open_setup_integration_page()
    setup.choose_cms(cms_name)
    setup.click_integration_download_plugin_button()
    assert setup.current_url() == market_link


# Check instruction link on email for developer.
@pytest.mark.parametrize('cms_name,doc_link', cms_tutorial_link)
def test_send_instruction(driver, cms_name, doc_link):
    setup = SetupPage(driver)
    login = LoginPage(driver)
    login.open_login_page()
    login.login_in()
    setup.open_setup_integration_page()
    setup.choose_cms(cms_name)
    setup.click_integration_send_instruction_button()
    setup.send_keys_developer_email(REAL_USER_EMAIL)
    setup.click_integration_send_instruction_to_developer_button()
    setup.open_url(check_email('TriggMine integration instruction'))
    assert setup.current_url() == doc_link


# Change text when choosing a CMS.
@pytest.mark.parametrize('cms_name', cms_list)
def test_check_changes_cms_name(driver, cms_name):
    setup = SetupPage(driver)
    login = LoginPage(driver)
    login.open_login_page()
    login.login_in()
    setup.open_setup_integration_page()
    setup.choose_cms(cms_name)
    assert setup.text_cms_name_tutorial_block() == cms_name
    assert setup.text_cms_name_credential_block() == cms_name


@pytest.mark.parametrize('email', ['!@#$%^&*', 'qwe!#$%^&*@gmail.com'])
def test_send_instruction_invalid_email(driver, email):
    setup = SetupPage(driver)
    login = LoginPage(driver)
    login.open_login_page()
    login.login_in()
    setup.open_setup_integration_page()
    setup.click_integration_send_instruction_button()
    setup.send_keys_developer_email(email)
    setup.click_integration_send_instruction_to_developer_button()
    assert setup.text_send_instruction_form_error_massage() == 'Invalid email address'
    assert setup.text_of_notification_massage() == 'Email is not valid!'


def test_check_api_url(driver):
    setup = SetupPage(driver)
    login = LoginPage(driver)
    login.open_login_page()
    login.login_in()
    setup.open_setup_integration_page()
    setup.check_api_form(setup.value_of_api_url())






