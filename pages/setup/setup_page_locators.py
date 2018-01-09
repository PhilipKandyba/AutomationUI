from selenium.webdriver.common.by import By


def select_cms(name):
    integration_cms_name = (By.XPATH, '//ul[@role="menu"]/li[contains(string(), "' + name + '")]')
    return integration_cms_name


class SetupPageLocators(object):
    H2_TITLE = (By.XPATH, '//h2')
    SETUP_NOTIFICATION_MASSAGE = (By.XPATH, '//i[@class="icon-attention"]/../..//p')
    SIGN_UP_POPUP_TITLE = (By.XPATH, '//div//button/../h3')
    SIGN_UP_POPUP_BUTTON = (By.XPATH, '//div/p/../button')
    SIGN_UP_SETTINGS_LINK = (By.XPATH, '//a[contains(@href,"/settings/account")]')
    SIGN_UP_NEXT_STEP_BUTTON = (By.XPATH, '//div/button')
    INTEGRATION_API_ULR_LABEL = (By.XPATH, '//label[contains(string(), "API URL")]')
    INTEGRATION_OPEN_CMS_LIST = (By.XPATH, '//div[contains(text(), "My website CMS is")]//i')
    INTEGRATION_WATCH_TUTORIAL_LINK = (By.XPATH, '//span[contains(string(), "Watch tutorial")]')
    INTEGRATION_DOWNLOAD_PLUGIN_BUTTON =(By.XPATH, '//button[contains(string(), "Download the plugin")]')
    INTEGRATION_SEND_INSTRUCTION_BUTTON =(By.XPATH, '//button[contains(string(), "Send instruction")]')
    INTEGRATION_SEND_INSTRUCTION_FORM_INPUT = (By.ID, 'idundefined')
    INTEGRATION_SEND_INSTRUCTION_FORM_ERROR_MASSAGE = (By.XPATH, '//input[@id="idundefined"]/../../span[2]/span')
    INTEGRATION_SEND_INSTRUCTION_FORM_SEND_BUTTON = (By.XPATH, '//small/../../div//button[contains(string(), "Send")]')
    INTEGRATION_CMS_NAME_TUTORIAL_BLOCK = (By.XPATH, '//h3[contains(string(), "2")]/div')
    INTEGRATION_CMS_NAME_CREDENTIAL_BLOCK = (By.XPATH, '//h3[contains(string(), "3")]/div')
    INTEGRATION_API_URL_INPUT = (By.XPATH, '//label[contains(string(), "URL")]/..//input')
