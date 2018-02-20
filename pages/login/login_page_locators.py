from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    EMAIL = (By.ID, 'tst-inpt-log-email')
    PASSWORD = (By.ID, 'tst-inpt-log-pswd')
    SUBMIT = (By.XPATH, '//button')
    NOTIFICATION_EMPTY_EMAIL_FIELD = (By.XPATH, '//*[@type="email"]/../../span[2]')
    NOTIFICATION_EMPTY_PASSWORD_FIELD = (By.XPATH, '//*[@type="password"]/../../../span[2]')
    FORM_NOTIFICATION = (By.XPATH, '//div/span/p')
    LINK_FORGOT_PASSWORD = (By.ID, 'tst-lnk-log-reset')
