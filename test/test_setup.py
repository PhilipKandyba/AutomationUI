import re
import pytest
from data.cms import cms_tutorial_link, cms_market_place, cms_list
from pages.setup.setup_page import SetupPage
from pages.login.login_page import LoginPage
from tools.check_email import check_email
from pages.account_settings.account_settings_page import AccountSettings
from request.plugin_integration import plugin_diagnostic


# First entering to cabinet. Showing popup.
@pytest.mark.skip
@pytest.mark.usefixtures("activating_setup_trial_modal")
def test_trial_modal(driver):
    setup = SetupPage(driver)
    login = LoginPage(driver)
    login.login_in()
    assert setup.is_popup_title()


# Check "Account setting" link.
def test_check_account_setting_link(driver):
    setup = SetupPage(driver)
    login = LoginPage(driver)
    settings = AccountSettings(driver)
    login.login_in()
    setup.open_setup_sign_up_page()
    setup.click_sign_up_settings_link()
    assert settings.is_save_changes_button()


# Going from "Sign in" to "Integration"
def test_from_setup_to_integration(driver):
    setup = SetupPage(driver)
    login = LoginPage(driver)
    login.login_in()
    setup.open_setup_sign_up_page()
    setup.click_sign_up_next_step_button()
    assert setup.is_integration_api_url_label()


# Checking link of documentation for all plugins.
@pytest.mark.usefixtures("login_in")
@pytest.mark.parametrize('cms_name,doc_link', cms_tutorial_link)
def test_check_cms_documentation(driver, cms_name, doc_link):
    setup = SetupPage(driver)
    setup.open_setup_integration_page()
    setup.choose_cms(cms_name)
    setup.click_integration_watch_tutorial_link()
    assert setup.current_url() == doc_link


# Checking link of market place for all plugins.
@pytest.mark.usefixtures("login_in")
@pytest.mark.parametrize('cms_name,market_link', cms_market_place)
def test_check_cms_market(driver, cms_name, market_link):
    setup = SetupPage(driver)
    setup.open_setup_integration_page()
    setup.choose_cms(cms_name)
    setup.click_integration_download_plugin_button()
    assert setup.current_url() == market_link


# Check instruction link on email for developer.
@pytest.mark.usefixtures("login_in")
@pytest.mark.parametrize('cms_name,doc_link', cms_tutorial_link)
def test_send_instruction(driver, cms_name, doc_link):
    setup = SetupPage(driver)
    setup.open_setup_integration_page()
    setup.choose_cms(cms_name)
    setup.click_integration_send_instruction_button()
    setup.send_keys_developer_email()
    setup.click_integration_send_instruction_to_developer_button()
    setup.open_url(check_email('TriggMine integration instruction'))
    assert setup.current_url() == doc_link


# Change text when choosing a CMS.
@pytest.mark.usefixtures("login_in")
@pytest.mark.parametrize('cms_name', cms_list)
def test_check_changes_cms_name(driver, cms_name):
    setup = SetupPage(driver)
    setup.open_setup_integration_page()
    setup.choose_cms(cms_name)
    assert setup.text_cms_name_tutorial_block() == cms_name
    assert setup.text_cms_name_credential_block() == cms_name


# Insert invalid data in email field on "Send instruction" form.
@pytest.mark.parametrize('email', ['!@#$%^&*', 'qwe!#$%^&*@gmail.com'])
def test_send_instruction_invalid_email(driver, email):
    setup = SetupPage(driver)
    login = LoginPage(driver)
    login.login_in()
    setup.open_setup_integration_page()
    setup.click_integration_send_instruction_button()
    setup.send_keys_developer_email(email)
    setup.click_integration_send_instruction_to_developer_button()
    assert setup.text_send_instruction_form_error_massage() == 'Invalid email address'
    assert setup.text_of_notification_massage() == 'Email is not valid!'


# Send new "Diagnostic" request and check massage about integration in banner.
def test_new_plugin_integration(driver):
    setup = SetupPage(driver)
    login = LoginPage(driver)
    login.login_in()
    setup.open_setup_integration_page()
    plugin_diagnostic()
    assert setup.text_of_plugin_status_block() == 'Trigmine integrated'


# Comparison of the API URL with a regular expression.
def test_check_api_url(driver):
    setup = SetupPage(driver)
    login = LoginPage(driver)
    login.login_in()
    setup.open_setup_integration_page()
    assert re.match('^(cabinet+[0-9.]+triggmine.com)', setup.value_of_api_url())


# Comparison API KEY on cabinet with API KEY in DB.
def test_check_correct_api_key(driver):
    setup = SetupPage(driver)
    login = LoginPage(driver)
    login.login_in()
    setup.open_setup_integration_page()
    assert setup.value_of_api_key() == setup.check_api_key_db()


# Comparison Shop URL on cabinet with Shop URL in DB.
def test_check_shop_url(driver):
    setup = SetupPage(driver)
    login = LoginPage(driver)
    login.login_in()
    setup.open_setup_integration_page()
    assert setup.value_shop_url() == setup.check_shop_url_in_db()


# Change Shop URL in cabinet and check in DB.
def test_change_shop_url(driver):
    setup = SetupPage(driver)
    login = LoginPage(driver)
    login.login_in()
    setup.open_setup_integration_page()
    new_shop_url = 'new-shop-url.com'
    setup.send_keys_shop_url(new_shop_url)
    setup.click_integration_confirm_shop_details_button()
    setup.open_setup_integration_page()
    assert setup.value_shop_url() == setup.check_shop_url_in_db()
    assert setup.value_shop_url() == new_shop_url






