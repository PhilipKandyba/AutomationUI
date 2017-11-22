from selenium.webdriver.common.by import By


class SignUpPageLocators(object):
    SHOP_URL_FIELD = (By.XPATH, '//input[@placeholder="Webshop URL"]')
    EMAIL_FIELD = (By.XPATH, '//input[@placeholder="Your email"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@placeholder="Your password (at least 6 charachters)"]')
    FIRST_NAME_FIELD = (By.XPATH, '//input[@placeholder="Your first name]')
    CONFIRMATION_BUTTON = (By.XPATH, '//button[contains(string(), "Get started")]')
    SHOP_URL_FIELD_REQUIRED_MASSAGE = (By.XPATH, '//label[contains(string(), "Webshop URL")]/../span[2]')
    EMAIL_FIELD_REQUIRED_MASSAGE = (By.XPATH, '//label[contains(string(), "Email")]/../span[2]')
    PASSWORD_FIELD_REQUIRED_MASSAGE = (By.XPATH, '//label[contains(string(), "Password")]/../span[2]')
    FIRST_NAME_FIELD_REQUIRED_MASSAGE = (By.XPATH, '//label[contains(string(), "First name")]/../span[2]')
