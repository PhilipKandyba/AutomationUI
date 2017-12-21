from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    EMAIL = (By.XPATH, '//*[@type="email"]')
    PASSWORD = (By.XPATH, '//*[@type="password"]')
    SUBMIT = (By.XPATH, '//button')
    NOTIFICATION_EMPTY_EMAIL_FIELD = (By.XPATH, '//*[@type="email"]/../../span[2]')
    NOTIFICATION_EMPTY_PASSWORD_FIELD = (By.XPATH, '//*[@type="password"]/../../../span[2]')
    FORM_NOTIFICATION = (By.XPATH, '//p')
    LINK_FORGOT_PASSWORD = (By.XPATH, '//a[contains(@href,"/forgetpassword")]')
