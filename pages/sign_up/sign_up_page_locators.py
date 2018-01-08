from selenium.webdriver.common.by import By


def select_industry(name):
    industry_name = (By.XPATH, '//span/span[contains(string(), "' + name + '")]')
    return industry_name


def selected_industry(name):
    selected_industry_name = (By.XPATH, '//div[contains(text(), "' + name + '")]')
    return selected_industry_name


class SignUpPageLocators(object):
    SHOP_URL_FIELD = (By.XPATH, '//label[contains(string(), "Webshop URL")]/..//input')
    EMAIL_FIELD = (By.XPATH, '//label[contains(string(), "Email")]/..//input')
    PASSWORD_FIELD = (By.XPATH, '//label[contains(string(), "Password")]/..//input')
    FIRST_NAME_FIELD = (By.XPATH, '//label[contains(string(), "First name")]/..//input')
    CONFIRMATION_BUTTON = (By.XPATH, '//button[contains(string(), "Get started")]')
    SHOP_URL_FIELD_ERROR_MASSAGE = (By.XPATH, '//label[contains(string(), "Webshop URL")]/../span[2]/span')
    EMAIL_FIELD_ERROR_MASSAGE = (By.XPATH, '//label[contains(string(), "Email")]/../span[2]/span')
    PASSWORD_FIELD_ERROR_MASSAGE = (By.XPATH, '//label[contains(string(), "Password")]/../span[2]/span')
    INDUSTRY_FIELD_ERROR_MASSAGE = (By.XPATH, '//div[contains(string(), "Select Industry")]/span')
    FIRST_NAME_FIELD_ERROR_MASSAGE = (By.XPATH, '//label[contains(string(), "First name")]/../span[2]/span')
    INDUSTRY_SELECT_BUTTON = (By.XPATH, '//button[1]')
    ERROR_NOTIFICATION = (By.XPATH, '//span/p')
    LINK_TERMS_OF_USE = (By.XPATH, '//a[contains(@href,"/terms-of-use")]')
    LINK_PRIVACY_POLICY = (By.XPATH, '//a[contains(@href,"/privacy-policy")]')
    HEADER_TERMS_OF_USE = (By.XPATH, '//h1[contains(string(), "Terms of Use & Privacy Policy")]')
    HEADER_PRIVACY_POLICY = (By.XPATH, '//h1[contains(string(), "Privacy Policy")]')

