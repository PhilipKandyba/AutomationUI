# Login in
def test_login_in(driver):
    driver.login_in('philip.kanduba@gmail.com', '123456')
    assert driver.is_he_title()


# All field is empty.
def test_empty_fields(driver):
    driver.click_login_button()
    assert driver.is_notification_from_email_field()
    assert driver.is_notification_from_password_field()


# Valid Email. Empty password field.
def test_email_valid_password_empty(driver):
    driver.enter_email('mail@em.com')
    driver.click_login_button()
    assert driver.is_notification_from_password_field()


# Not valid Email. Empty password field.
def test_email_not_valid_password_empty(driver):
    driver.enter_email('some_text')
    driver.click_login_button()
    assert driver.text_notification_from_email_field() == 'Invalid email address'


# Empty Email field. Valid password.
def test_email_empty_password_valid(driver):
    driver.enter_password('123456')
    driver.click_login_button()
    assert driver.text_notification_from_email_field() == 'Required'


# Not valid Email. Valid password.
def test_email_not_valid_pasword_valid(driver):
    driver.enter_email('some_text')
    driver.enter_password('123456')
    driver.click_login_button()
    assert driver.text_notification_from_email_field() == 'Invalid email address'


# Not register user. Valid password.
def test_unregistered_user_valid_password(driver):
    driver.enter_email('qwe_test@qwe.com')
    driver.enter_password('123456')
    driver.click_login_button()
    assert driver.is_form_notification()
    assert driver.text_form_notification() == 'The user name or password is incorrect.'


# User not confirmed own email.

def test_user_not_confirm_email(driver):
    driver.enter_email('philip.kanduba+test4@gmail.com')
    driver.enter_password('123456')
    driver.click_login_button()
    assert driver.is_form_notification()
    assert driver.text_form_notification() == 'User have to confirm his email'



