import pytest
from pages.login.login_page import LoginPage
from tools.postgresql import select_user_email
from data.incorrect_user_data import incorrect_user_name
from pages.profile_settings.profile_settings_page import ProfileSettings


@pytest.mark.usefixtures("login_in")
def test_open_profile_settings(driver):
    profile_settings = ProfileSettings(driver)
    profile_settings.open_profile_settings_page()
    assert profile_settings.is_profile_settings_header()


@pytest.mark.usefixtures("login_in")
def test_check_user_first_name(driver):
    profile_settings = ProfileSettings(driver)
    profile_settings.open_profile_settings_page()
    assert profile_settings.value_first_name() == profile_settings.check_first_name_in_db()


@pytest.mark.usefixtures("login_in")
def test_empty_first_name_field(driver):
    profile_settings = ProfileSettings(driver)
    profile_settings.open_profile_settings_page()
    profile_settings.clear_first_name_field()
    profile_settings.click_save_changes_button()
    assert profile_settings.text_error_notification() == 'Required'
    assert profile_settings.text_first_name_field_notification() == 'Required'


@pytest.mark.usefixtures("login_in")
@pytest.mark.parametrize('name', incorrect_user_name)
def test_incorrect_first_name(driver, name):
    profile_settings = ProfileSettings(driver)
    profile_settings.open_profile_settings_page()
    profile_settings.send_keys_first_name_field(name)
    profile_settings.click_save_changes_button()
    assert profile_settings.text_error_notification() == 'Field Name can only match letters, "-" and spaces'
    assert profile_settings.text_first_name_field_notification() == 'Field Name can only match letters, "-" and spaces'


@pytest.mark.usefixtures("login_in")
def test_empty_last_name_field(driver):
    profile_settings = ProfileSettings(driver)
    profile_settings.open_profile_settings_page()
    profile_settings.clear_last_name_field()
    profile_settings.click_save_changes_button()
    assert profile_settings.text_error_notification() == 'Required'
    assert profile_settings.text_last_name_field_notification() == 'Required'


@pytest.mark.usefixtures("login_in")
@pytest.mark.parametrize('name', incorrect_user_name)
def test_incorrect_last_name(driver, name):
    profile_settings = ProfileSettings(driver)
    profile_settings.open_profile_settings_page()
    profile_settings.send_keys_last_name_field(name)
    profile_settings.click_save_changes_button()
    assert profile_settings.text_error_notification() == 'Field Name can only match letters, "-" and spaces'
    assert profile_settings.text_last_name_field_notification() == 'Field Name can only match letters, "-" and spaces'


@pytest.mark.usefixtures("login_in")
def test_check_email(driver):
    profile_settings = ProfileSettings(driver)
    profile_settings.open_profile_settings_page()
    assert profile_settings.value_email() == select_user_email()


@pytest.mark.scip
@pytest.mark.usefixtures("login_in")
def test_change_password(driver):
    profile_settings = ProfileSettings(driver)
    login_in = LoginPage(driver)
    profile_settings.open_profile_settings_page()
    profile_settings.send_keys_current_password('1234567890')
    profile_settings.send_keys_new_password('123456')
    profile_settings.click_save_changes_button()
    login_in.login_in(password='123456')


@pytest.mark.usefixtures("login_in")
def test_empty_current_password_field(driver):
    profile_settings = ProfileSettings(driver)
    profile_settings.open_profile_settings_page()
    profile_settings.send_keys_current_password('123456')
    profile_settings.clear_new_password_field()
    profile_settings.click_save_changes_button()
    assert profile_settings.text_error_notification() == 'Please type another password. Min length is 6'
    assert profile_settings.text_new_password_field_notification() == 'Please type another password. Min length is 6'


@pytest.mark.usefixtures("login_in")
def test_empty_new_password_field(driver):
    profile_settings = ProfileSettings(driver)
    profile_settings.open_profile_settings_page()
    profile_settings.send_keys_new_password('123456')
    profile_settings.clear_current_password_field()
    profile_settings.click_save_changes_button()
    assert profile_settings.text_error_notification() == 'Please type another password. Min length is 6'
    assert profile_settings.text_current_password_field_notification() == 'Please type another password. Min length is 6'

