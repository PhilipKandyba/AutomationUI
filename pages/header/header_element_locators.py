from selenium.webdriver.common.by import By


class HeaderElementLocators(object):
    LOGO_ICON = (By.XPATH, '//a/i')
    IMG_LOGO = (By.XPATH, '//img[contains(@title,"Triggmine")]')
    LINK_LOGIN_IN = (By.XPATH, '//a[contains(@href,"/login")]')
    LINK_SIGN_UP = (By.XPATH, '//a[contains(@href,"/signup")]')
