# All field is empty.
def test_empty_fields(login):
    login.click_login_button()
    assert login.notification_from_email_field().is_displayed()
    assert login.notification_from_password_field().is_displayed()


# Valid Email. Empty password field.
def test_email_valid_password_empty(driver):
    driver.enter_email('mail@em.com')
    driver.click_login_button()
    assert driver.notification_from_password_field().is_displayed()


# Not valid Email. Empty password field.
def test_email_not_valid_password_empty(driver):
    driver.enter_email('some_text')
    driver.click_login_button()
    assert driver.notification_from_email_field().text == 'Invalid email address'


# Empty Email field. Valid password.
def test_email_empty_password_valid(driver):
    driver.enter_password('123456')
    driver.click_login_button()
    assert driver.notification_from_email_field().text == 'Required'


# Not valid Email. Valid password.
def test_email_not_valid_pasword_valid(driver):
    driver.enter_email('some_text')
    driver.enter_password('123456')
    driver.click_login_button()
    assert driver.notification_from_email_field().text == 'Invalid email address'


# Not register user. Valid password.
def test_unregistered_user_valid_password(driver):
    driver.enter_email('qwe_test@qwe.com')
    driver.enter_password('123456')
    driver.click_login_button()
    assert driver.form_notification().is_displayed()
    assert driver.form_notification().text == 'The user name or password is incorrect.'


# User not confirmed own email.

def test_user_not_confirm_email(driver):
    driver.enter_email('philip.kanduba+test4@gmail.com')
    driver.enter_password('123456')
    driver.click_login_button()
    assert driver.form_notification().is_displayed()
    assert driver.form_notification().text == 'User have to confirm his email'



