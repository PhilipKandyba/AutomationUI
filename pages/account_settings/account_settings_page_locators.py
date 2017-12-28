from selenium.webdriver.common.by import By


class AccountSettingsPageLocators(object):
    SAVE_CHANGES_BUTTON = (By.XPATH, '//div/label/../../../button')
