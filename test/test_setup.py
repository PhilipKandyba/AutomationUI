import re
import pytest
from data.cms import cms_tutorial_link, cms_market_place, cms_list
from pages.setup.setup_page import SetupPage
from pages.login.login_page import LoginPage
from pages.dashboard.dashboard_page import DashboardPage
from tools.check_email import check_email
from pages.account_settings.account_settings_page import AccountSettings
from request.plugin_integration import plugin_diagnostic
from data.users import NEW_USER_EMAIL


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
@pytest.mark.skip
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
    new_shop_url = 'http://new-shop-url.com'
    setup.send_keys_shop_url(new_shop_url)
    setup.click_integration_confirm_shop_details_button()
    setup.open_setup_integration_page()
    assert setup.value_shop_url() == setup.check_shop_url_in_db()
    assert setup.value_shop_url() == new_shop_url


@pytest.mark.usefixtures("login_in")
# Check USD like default currency.
def test_check_default_currency(driver):
    setup = SetupPage(driver)
    setup.open_setup_integration_page()
    assert setup.is_currency_usd()


@pytest.mark.usefixtures("login_in", "update_currency")
# Change currency from USD to AED and check in DB.
# Check changes of from USD to AED currency symbol.
def test_check_default_currency(driver):
    setup = SetupPage(driver)
    dashboard = DashboardPage(driver)
    setup.open_setup_integration_page()
    setup.click_integration_open_currency_list()
    setup.click_integration_currency_aed()
    setup.click_integration_confirm_shop_details_button()
    assert setup.check_shop_currency_in_db() == 'AED'
    assert dashboard.text_currency_symbol() == 'د.إ'


@pytest.mark.usefixtures("login_in")
def test_check_default_sender_name(driver):
    setup = SetupPage(driver)
    setup.open_setup_email_design()
    assert setup.text_email_design_sender_name() == setup.check_first_name_in_db()


@pytest.mark.usefixtures("login_in")
def test_check_default_sender_email(driver):
    setup = SetupPage(driver)
    setup.open_setup_email_design()
    assert setup.text_email_design_sender_email() == setup.check_email_from_in_db()


@pytest.mark.usefixtures("login_in")
def test_add_new_sender(driver):
    setup = SetupPage(driver)
    setup.open_setup_email_design()
    setup.click_email_design_open_senders_list()
    setup.click_email_design_add_new_sender_button()
    setup.send_keys_new_sender_name('test')
    setup.send_keys_new_sender_email(NEW_USER_EMAIL)
    setup.click_email_design_add_new_sender_form_confirmation_button()
    setup.open_url(check_email('Activate your email'))
    assert setup.text_email_design_add_sender_success_page_header() == 'Email successfully verified'


@pytest.mark.usefixtures("login_in")
@pytest.mark.parametrize('email', ['!@#$%^&*', 'qwe!#$%^&*@gmail.com', 'qwe.com', '@com.ua'])
def test_add_new_sender(driver, email):
    setup = SetupPage(driver)
    setup.open_setup_email_design()
    setup.click_email_design_open_senders_list()
    setup.click_email_design_add_new_sender_button()
    setup.send_keys_new_sender_name('test')
    setup.send_keys_new_sender_email(email)
    setup.click_email_design_add_new_sender_form_confirmation_button()
    assert setup.text_of_notification_massage() == 'Sender email is not valid'
    assert setup.text_email_design_sender_email_form_email_field_error() == 'Invalid email address'


