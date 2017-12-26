from tools.check_email import check_email
from pages.login.login_page import LoginPage
from pages.sign_up.sign_up_page import SignUpPage
from pages.header.header_element import HeaderElement
from pages.dashboard.dashboard_page import DashboardPage
from pages.resset_pasword.resset_password_page import ResetPasswordPage
from data.users import RESET_PASSWORD_USER_EMAIL, RESET_PASSWORD_USER_NEW_PASSWORD


# Empty email field. Assert "Required" massage.
def test_empty_email_field(driver):
    password = ResetPasswordPage(driver)
    password.open_password_page()
    password.click_reset_password_button()
    assert password.is_email_field_error_massage()


def test_incorrect_email(driver):
    password = ResetPasswordPage(driver)
    password.open_password_page()
    password.send_keys_email_field('!@#$%^&*()+')
    password.click_reset_password_button()
    assert password.text_email_field() == 'Invalid email address'


def test_not_existing_user(driver):
    password = ResetPasswordPage(driver)
    password.open_password_page()
    email = 'qwe@qwe.com'
    password.send_keys_email_field(email)
    password.click_reset_password_button()
    assert password.text_of_notification() == "Cannot find user with email: " + email + " or user's email isn't" \
                                                                                        " confirmed"


# Check link "login"
def test_check_sign_up_link(driver):
    password = ResetPasswordPage(driver)
    sign_up = SignUpPage(driver)
    header = HeaderElement(driver)
    password.open_password_page()
    header.click_sign_up_link()
    assert sign_up.is_sign_up_button()


# Check link on Logo
def test_check_img_link(driver):
    password = ResetPasswordPage(driver)
    login = LoginPage(driver)
    header = HeaderElement(driver)
    password.open_password_page()
    header.click_logo()
    assert login.is_login_button()


# Change password
def test_change_password(driver):
    password = ResetPasswordPage(driver)
    login = LoginPage(driver)
    dashboard = DashboardPage(driver)
    password.open_password_page()
    password.send_keys_email_field(RESET_PASSWORD_USER_EMAIL)
    password.click_reset_password_button()
    password.open_url(check_email('Password recovery'))
    password.send_keys_password_field(RESET_PASSWORD_USER_NEW_PASSWORD)
    password.click_reset_password_button()
    login.open_login_page()
    login.login_in(RESET_PASSWORD_USER_EMAIL, RESET_PASSWORD_USER_NEW_PASSWORD + '1')
    assert dashboard.is_statistic_header()