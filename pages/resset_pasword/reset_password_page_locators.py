from selenium.webdriver.common.by import By


class ResetPasswordPageLocators(object):
    HEADER_RESET_PASSWORD = (By.XPATH, '//h1')
    RESET_PASSWORD_BUTTON = (By.XPATH, '//form/button')
    EMAIL_FIELD = (By.XPATH, '//input')
    PASSWORD_FIELD = (By.XPATH, '//input[@type="password"]')
    EMAIL_FIELD_ERROR_MASSAGE = (By.XPATH, '//span/span')
    ERROR_NOTIFICATION = (By.XPATH, '//span/p')
