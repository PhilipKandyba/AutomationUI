from Pages.Login.LoginPage import LoginPage
from Pages.Setup.SetupPage import SetupPage


# Login in
def test_login_in(login, setup):
    login.login_in('philip.kanduba@gmail.com', '123456')
    assert setup.is_he_title()

# All field is empty.
def test_empty_fields(login):
    login.click_login_button()
    assert login.is_notification_from_email_field()
    assert login.is_notification_from_password_field()


# Valid Email. Empty password field.
def test_email_valid_password_empty(login):
    login.enter_email('mail@em.com')
    login.click_login_button()
    assert login.is_notification_from_password_field()


# Not valid Email. Empty password field.
def test_email_not_valid_password_empty(login):
    login.enter_email('some_text')
    login.click_login_button()
    assert login.text_notification_from_email_field() == 'Invalid email address'


# Empty Email field. Valid password.
def test_email_empty_password_valid(login):
    login.enter_password('123456')
    login.click_login_button()
    assert login.text_notification_from_email_field() == 'Required'


# Not valid Email. Valid password.
def test_email_not_valid_pasword_valid(login):
    login.enter_email('some_text')
    login.enter_password('123456')
    login.click_login_button()
    assert login.text_notification_from_email_field() == 'Invalid email address'


# Not register user. Valid password.
def test_unregistered_user_valid_password(login):
    login.enter_email('qwe_test@qwe.com')
    login.enter_password('123456')
    login.click_login_button()
    assert login.is_form_notification()
    assert login.text_form_notification() == 'The user name or password is incorrect.'


# User not confirmed own email.
def test_user_not_confirm_email(login):
    login.enter_email('philip.kanduba+test4@gmail.com')
    login.enter_password('123456')
    login.click_login_button()
    assert login.is_form_notification()
    assert login.text_form_notification() == 'User have to confirm his email'



