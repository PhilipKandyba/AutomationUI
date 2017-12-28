from selenium.webdriver.common.by import By


def select_cms(name):
    integration_cms_name = (By.XPATH, '//ul[@role="menu"]/li[contains(string(), "' + name + '")]')
    return integration_cms_name


class SetupPageLocators(object):
    H2_TITLE = (By.XPATH, '//h2')
    SIGN_UP_POPUP_TITLE = (By.XPATH, '//div//button/../h3')
    SIGN_UP_POPUP_BUTTON = (By.XPATH, '//div/p/../button')
    SIGN_UP_SETTINGS_LINK = (By.XPATH, '//a[contains(@href,"/settings/account")]')
    SIGN_UP_NEXT_STEP_BUTTON = (By.XPATH, '//div/button')
    INTEGRATION_API_ULR_LABEL = (By.XPATH, '//label[contains(string(), "API URL")]')
    INTEGRATION_OPEN_CMS_LIST = (By.CLASS_NAME, 'icon-arrow-down-bold')
