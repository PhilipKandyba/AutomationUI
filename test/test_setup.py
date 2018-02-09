import re
import pytest
from data.currencies import currencies_list
from data.cms import cms_tutorial_link, cms_market_place, cms_list
from data.industries import industries_list
from data.users import NEW_USER_EMAIL, NEW_SHOP_URL
from data.incorrect_emails import incorrect_emails_list
from pages.setup.setup_page import SetupPage
from pages.dashboard.dashboard_page import DashboardPage
from tools.check_email import check_email
from pages.account_settings.account_settings_page import AccountSettings
from request.plugin_integration import plugin_diagnostic


# Going from "Sign in" to "Integration"
# First entering to cabinet. Showing popup.
@pytest.mark.usefixtures("login_in", "activating_setup_trial_modal")
def test_trial_modal(driver):
    setup = SetupPage(driver)
    setup.open_setup_sign_up_page()
    setup.click_sign_up_next_step_button()
    assert setup.is_popup_title()
    assert setup.is_integration_api_url_label()


# Check "Account setting" link.
@pytest.mark.usefixtures("login_in")
def test_check_account_setting_link(driver):
    setup = SetupPage(driver)
    settings = AccountSettings(driver)
    setup.open_setup_sign_up_page()
    setup.click_sign_up_settings_link()
    assert settings.is_save_changes_button()


# Checking link of documentation for all plugins.
@pytest.mark.usefixtures("login_in", "clear_plugin_table")
@pytest.mark.parametrize('cms_name,doc_link', cms_tutorial_link)
def test_check_cms_documentation(driver, cms_name, doc_link):
    setup = SetupPage(driver)
    setup.open_setup_integration_page()
    setup.choose_cms(cms_name)
    setup.click_integration_watch_tutorial_link()
    assert setup.current_url() == doc_link


# Checking link of market place for all plugins.
@pytest.mark.usefixtures("login_in", "clear_plugin_table")
@pytest.mark.parametrize('cms_name,market_link', cms_market_place)
def test_check_cms_market(driver, cms_name, market_link):
    setup = SetupPage(driver)
    setup.open_setup_integration_page()
    setup.choose_cms(cms_name)
    setup.click_integration_download_plugin_button()
    assert setup.current_url() == market_link


# Check instruction link on email for developer.
@pytest.mark.usefixtures("login_in", "clear_plugin_table")
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
@pytest.mark.usefixtures("login_in", "clear_plugin_table")
@pytest.mark.parametrize('cms_name', cms_list)
def test_check_changes_cms_name(driver, cms_name):
    setup = SetupPage(driver)
    setup.open_setup_integration_page()
    setup.choose_cms(cms_name)
    assert setup.text_cms_name_tutorial_block() == cms_name
    assert setup.text_cms_name_credential_block() == cms_name


# Insert invalid data in email field on "Send instruction" form.
@pytest.mark.usefixtures("login_in")
@pytest.mark.parametrize('email', incorrect_emails_list)
def test_send_instruction_invalid_email(driver, email):
    setup = SetupPage(driver)
    setup.open_setup_integration_page()
    setup.click_integration_send_instruction_button()
    setup.send_keys_developer_email(email)
    setup.click_integration_send_instruction_to_developer_button()
    assert setup.text_send_instruction_form_error_massage() == 'Invalid email address'
    assert setup.text_of_notification_massage() == 'Email is not valid!'


# Send new "Diagnostic" request and check massage about integration in banner.
@pytest.mark.usefixtures("login_in")
def test_new_plugin_integration(driver):
    setup = SetupPage(driver)
    setup.open_setup_integration_page()
    plugin_diagnostic()
    assert setup.text_of_plugin_status_block() == 'Trigmine integrated'


# Comparison of the API URL with a regular expression.
@pytest.mark.usefixtures("login_in")
def test_check_api_url(driver):
    setup = SetupPage(driver)
    setup.open_setup_integration_page()
    assert re.match('^(cabinet+[0-9.]+triggmine.com)', setup.value_of_api_url())
    assert re.split('^(cabinet+[0-9]+)', setup.value_of_api_url())[1] == setup.check_user_name_db()


# Comparison API KEY on cabinet with API KEY in DB.
@pytest.mark.usefixtures("login_in")
def test_check_correct_api_key(driver):
    setup = SetupPage(driver)
    setup.open_setup_integration_page()
    assert setup.value_of_api_key() == setup.check_api_key_db()


@pytest.mark.usefixtures("login_in")
# Comparison Shop URL on cabinet with Shop URL in DB.
def test_check_shop_url(driver):
    setup = SetupPage(driver)
    setup.open_setup_integration_page()
    assert setup.value_shop_url() == setup.check_shop_url_in_db()


# Change Shop URL in cabinet and check in DB.
@pytest.mark.usefixtures("login_in")
def test_change_shop_url(driver):
    setup = SetupPage(driver)
    setup.open_setup_integration_page()
    setup.send_keys_shop_url(NEW_SHOP_URL)
    setup.click_integration_confirm_shop_details_button()
    assert setup.text_of_notification_massage() == 'Shop details updated'
    setup.open_setup_integration_page()
    assert setup.value_shop_url() == setup.check_shop_url_in_db()
    assert setup.value_shop_url() == NEW_SHOP_URL


# Change currency from USD to AED and check in DB.
# Check changes of from USD to AED currency symbol.
@pytest.mark.skip
@pytest.mark.parametrize('name,symbol', currencies_list)
@pytest.mark.usefixtures("login_in")
def test_check_default_currency(driver, name, symbol):
    setup = SetupPage(driver)
    dashboard = DashboardPage(driver)
    setup.open_setup_integration_page()
    setup.click_integration_open_currency_list()
    setup.click_integration_currency_name(name)
    setup.click_integration_confirm_shop_details_button()
    assert setup.text_of_notification_massage() == 'Shop details updated'
    assert setup.check_shop_currency_in_db() == name
    assert dashboard.text_currency_symbol() == symbol


# Check user from email and user name.
@pytest.mark.usefixtures("login_in")
def test_check_default_sender_name_email(driver):
    setup = SetupPage(driver)
    setup.open_setup_email_design()
    assert setup.text_email_design_sender_name() == setup.check_first_name_in_db()
    assert setup.text_email_design_sender_email() == setup.check_email_from_in_db()


# Add new sender email and validate.
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


# Add new sender with incorrect email.
@pytest.mark.usefixtures("login_in")
@pytest.mark.parametrize('email', incorrect_emails_list)
def test_add_new_sender_with_incorrect_email(driver, email):
    setup = SetupPage(driver)
    setup.open_setup_email_design()
    setup.click_email_design_open_senders_list()
    setup.click_email_design_add_new_sender_button()
    setup.send_keys_new_sender_name('test')
    setup.send_keys_new_sender_email(email)
    setup.click_email_design_add_new_sender_form_confirmation_button()
    assert setup.text_of_notification_massage() == 'Sender email is not valid'
    assert setup.text_email_design_sender_email_form_email_field_error() == 'Invalid email address'


# Add incorrect support email.
@pytest.mark.usefixtures("login_in", "add_logo_image")
@pytest.mark.parametrize('email', incorrect_emails_list)
def test_add_support_email_invalid_data(driver, email):
    setup = SetupPage(driver)
    setup.open_setup_email_design()
    setup.click_email_design_add_support_email_button()
    setup.send_keys_new_support_email(email)
    setup.click_email_design_add_support_email_form_button()
    assert setup.text_of_notification_massage() == 'Support email is not valid'


# Add new support email and check in DB.
@pytest.mark.usefixtures("login_in", "add_logo_image")
def test_add_support_email(driver):
    setup = SetupPage(driver)
    setup.open_setup_email_design()
    setup.click_email_design_add_support_email_button()
    setup.send_keys_new_support_email(NEW_USER_EMAIL)
    setup.click_email_design_add_support_email_form_button()
    setup.click_email_design_confirmation_button()
    assert setup.text_email_design_support_email() == NEW_USER_EMAIL
    assert setup.text_email_design_support_email() == setup.check_support_email_in_db()


# Select industries, check changes on page and check in DB.
@pytest.mark.parametrize('industry_name,industry_id', industries_list)
@pytest.mark.usefixtures("login_in", "add_logo_image", "add_support_email")
def test_choose_industries(driver, industry_name, industry_id):
    setup = SetupPage(driver)
    setup.open_setup_email_design()
    setup.click_email_design_open_industries_list()
    setup.click_email_design_industry(industry_name)
    setup.click_email_design_confirmation_button()
    assert setup.text_email_design_current_industry() == industry_name
    assert industry_id == setup.check_industry_id_in_db()

