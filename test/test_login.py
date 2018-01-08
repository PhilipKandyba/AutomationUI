from data import url
from pages.login.login_page import LoginPage
from pages.sign_up.sign_up_page import SignUpPage
from pages.header.header_element import HeaderElement
from pages.dashboard.dashboard_page import DashboardPage
from pages.resset_pasword.resset_password_page import ResetPasswordPage
from data.users import REAL_USER_EMAIL, NEW_USER_PASSWORD, UNCONFIRMED_USER_EMAIL


# login in
def test_login_in(driver):
    login = LoginPage(driver)
    dashboard = DashboardPage(driver)
    login.open_login_page()
    login.login_in(REAL_USER_EMAIL, NEW_USER_PASSWORD)
    assert dashboard.is_statistic_header()


# All field is empty.
def test_empty_fields(driver):
    login = LoginPage(driver)
    login.open_login_page()
    login.click_login_button()
    assert login.is_notification_from_email_field()
    assert login.is_notification_from_password_field()


# Valid Email. Empty password field.
def test_email_valid_password_empty(driver):
    login = LoginPage(driver)
    login.open_login_page()
    login.enter_email('mail@em.com')
    login.click_login_button()
    assert login.is_notification_from_password_field()


# Not valid Email. Empty password field.
def test_email_not_valid_password_empty(driver):
    login = LoginPage(driver)
    login.open_login_page()
    login.enter_email('some_text')
    login.click_login_button()
    assert login.text_notification_from_email_field() == 'Invalid email address'


# Empty Email field. Valid password.
def test_email_empty_password_valid(driver):
    login = LoginPage(driver)
    login.open_login_page()
    login.enter_password('123456')
    login.click_login_button()
    assert login.text_notification_from_email_field() == 'Required'


# Not valid Email. Valid password.
def test_email_not_valid_password_valid(driver):
    login = LoginPage(driver)
    login.open_login_page()
    login.enter_email('some_text')
    login.enter_password('123456')
    login.click_login_button()
    assert login.text_notification_from_email_field() == 'Invalid email address'


# Not register user. Valid password.
def test_unregistered_user_valid_password(driver):
    login = LoginPage(driver)
    login.open_login_page()
    login.enter_email('qwe_test@qwe.com')
    login.enter_password('123456')
    login.click_login_button()
    assert login.text_form_notification() == 'The user name or password is incorrect.'


# User not confirmed own email.
def test_user_not_confirm_email(driver):
    login = LoginPage(driver)
    login.open_login_page()
    login.enter_email(UNCONFIRMED_USER_EMAIL)
    login.enter_password('123456')
    login.click_login_button()
    assert login.is_form_notification()
    assert login.text_form_notification() == 'User have to confirm his email'


# Real email, incorrect password.
def test_correct_email_incorrect_password(driver):
    login = LoginPage(driver)
    login.open_login_page()
    login.enter_email(REAL_USER_EMAIL)
    login.enter_password('654321')
    login.click_login_button()
    assert login.text_form_notification() == 'The user name or password is incorrect.'


# Check "Sign up" link
def test_check_sign_up_link(driver):
    login = LoginPage(driver)
    sign_up = SignUpPage(driver)
    header = HeaderElement(driver)
    login.open_login_page()
    header.click_sign_up_link()
    assert sign_up.is_sign_up_button()


# Check link on Logo
def test_check_img_link(driver):
    login = LoginPage(driver)
    header = HeaderElement(driver)
    login.open_login_page()
    header.click_logo()
    assert login.current_url() == url.TRIGGMINE_LENDING


# Check link "Reset password"
def test_check_reset_password_link(driver):
    login = LoginPage(driver)
    password_reset = ResetPasswordPage(driver)
    login.open_login_page()
    login.click_link_forgot_password()
    assert password_reset.is_reset_password_page_header()


def test_check_intercom_chat(driver):
    login = LoginPage(driver)
    dashboard = DashboardPage(driver)
    login.open_login_page()
    login.login_in(REAL_USER_EMAIL, NEW_USER_PASSWORD)
    assert dashboard.is_intercom_frame()
