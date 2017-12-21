import pytest
from Pages.Login.LoginPage import LoginPage
from Pages.SignUp.SignUpPage import SignUpPage
from Pages.Header.HeaderElement import HeaderElement
from Pages.SignUp.SignUpSuccessPage import SingUpSuccessPage
from Data.Users import REAL_USER_EMAIL as EMAIL
from Data.Users import REAL_USER_PASSWORD as PASSWORD
from Data.Users import REAL_USER_FIRST_NAME as NAME
from Data.Users import TEST_WEB_SHOP_URL as SHOP
from Data.Users import NEW_USER_EMAIL as NEW_EMAIL
from Data.Users import NEW_USER_PASSWORD as NEW_PASSWORD
from Data.Users import NEW_USER_FIRST_NAME as NEW_NAME
from Data.Users import UNCONFIRMED_USER_EMAIL as UNCONFIRMED_EMAIL
from Data.Industry import INDUSTRY
from Tools.CheckEmail import check_email
from Data import URL


# All fields is empty. Check massage "Required"
def test_all_required_massage_is_displayed(driver):
    sign_up = SignUpPage(driver)
    sign_up.open_signup_page()
    sign_up.is_all_required_massage()


# Shop url. Massage: "Required"
def test_shop_url_required_massage(driver):
    sign_up = SignUpPage(driver)
    sign_up.open_signup_page()
    sign_up.send_keys_email_field('some@email.com')
    sign_up.send_keys_password('some_text')
    sign_up.send_keys_first_name_field('some_name')
    sign_up.click_signup_button()
    assert sign_up.is_shop_url_field_required_massage()


# Email. Massage: "Required"
def test_email_required_massage(driver):
    sign_up = SignUpPage(driver)
    sign_up.open_signup_page()
    sign_up.send_keys_shop_url_field('some-url.com')
    sign_up.send_keys_password('some_text')
    sign_up.send_keys_first_name_field('some_name')
    sign_up.click_signup_button()
    assert sign_up.is_email_field_required_massage()


# Password. Massage: "Required"
def test_password_url_required_massage(driver):
    sign_up = SignUpPage(driver)
    sign_up.open_signup_page()
    sign_up.send_keys_email_field('some@email.com')
    sign_up.send_keys_shop_url_field('some-url.com')
    sign_up.send_keys_first_name_field('some_name')
    sign_up.click_signup_button()
    assert sign_up.is_password_field_required_massage()


# First name. Massage: "Required"
def test_first_name_url_required_massage(driver):
    sign_up = SignUpPage(driver)
    sign_up.open_signup_page()
    sign_up.send_keys_email_field('some@email.com')
    sign_up.send_keys_shop_url_field('some-url.com')
    sign_up.send_keys_password('some_text')
    sign_up.click_signup_button()
    assert sign_up.is_first_name_field_required_massage()


# First name. Massage: "Field Name can only match letters, "-" and spaces"
def test_wrong_first_name(driver):
    sign_up = SignUpPage(driver)
    sign_up.open_signup_page()
    sign_up.send_keys_first_name_field('!@#$%Name^&*()')
    sign_up.click_signup_button()
    assert sign_up.text_first_name_field_error_massage() == 'Field Name can only match letters, "-" and spaces'


# Presence of all industries.
def test_check_industries(driver):
    sign_up = SignUpPage(driver)
    sign_up.open_signup_page()
    sign_up.check_industry_list(INDUSTRY)


# The existing user.
def test_existing_user(driver):
    sign_up = SignUpPage(driver)
    sign_up.open_signup_page()
    sign_up.fill_the_form(SHOP, EMAIL, NAME, PASSWORD, INDUSTRY[1])
    sign_up.click_signup_button()
    assert sign_up.text_of_notification() == 'User with email ' + EMAIL + ' already exists!'


# New registration.
@pytest.mark.skip(reason='Skipping new registration')
def test_new_registration(driver):
    sign_up = SignUpPage(driver)
    login = LoginPage(driver)
    sign_up_success = SingUpSuccessPage(driver)
    sign_up.open_signup_page()
    sign_up.fill_the_form(SHOP, NEW_EMAIL, NEW_NAME, NEW_PASSWORD, INDUSTRY[1])
    sign_up.click_signup_button()
    sign_up.open_url(check_email('Activate'))
    sign_up_success.is_confirm_header()
    sign_up_success.click_go_to_account_button()
    assert login.is_login_button()


# Registration with an unconfirmed email.
def test_registration_on_unconfirmed_email(driver):
    sign_up = SignUpPage(driver)
    sign_up.open_signup_page()
    sign_up.fill_the_form(SHOP, UNCONFIRMED_EMAIL, NEW_NAME, NEW_PASSWORD, INDUSTRY[5])
    sign_up.click_signup_button()
    assert sign_up.text_of_notification() == "Email " + UNCONFIRMED_EMAIL + " isn't confirmed. Please check your " \
                                                                            "mailbox for email validation"


# User enter shot password (3 symbol)
def test_short_password(driver):
    sign_up = SignUpPage(driver)
    sign_up.open_signup_page()
    sign_up.fill_the_form(SHOP, NEW_EMAIL, NEW_NAME, '123', INDUSTRY[5])
    sign_up.click_signup_button()
    assert sign_up.text_password_field_error_massage() == 'Please type another password. Min length is 6'


# Check link "Terms of use"
def test_check_terms_of_use(driver):
    sign_up = SignUpPage(driver)
    sign_up.open_signup_page()
    sign_up.click_terms_of_use()
    assert sign_up.text_terms_of_use_header() == 'Terms of Use & Privacy Policy'


# Check link "Privacy policy"
def test_check_privacy_policy(driver):
    sign_up = SignUpPage(driver)
    sign_up.open_signup_page()
    sign_up.click_privacy_policy()
    assert sign_up.text_privacy_policy_header() == 'Privacy Policy'


# Check link "Login"
def test_check_login_link(driver):
    sign_up = SignUpPage(driver)
    login = LoginPage(driver)
    header = HeaderElement(driver)
    sign_up.open_signup_page()
    header.click_login_link()
    assert login.is_login_button()


# Check link on Logo
def test_check_img_link(driver):
    sign_up = SignUpPage(driver)
    header = HeaderElement(driver)
    sign_up.open_signup_page()
    header.click_logo()
    assert sign_up.current_url() == URL.TRIGGMINE_LENDING
