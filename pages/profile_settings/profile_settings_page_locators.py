from selenium.webdriver.common.by import By


class ProfileSettingsPageLocators(object):
    HEADER = (By.XPATH, '//h2[contains(string(), "Personal details")]')
    FIRST_NAME_FIELD = (By.XPATH, '//label[contains(string(), "First name")]/..//input')
    LAST_NAME_FIELD = (By.XPATH, '//label[contains(string(), "Last name")]/..//input')
    EMAIL_FIELD = (By.XPATH, '//label[contains(string(), "Email")]/..//input')
    CURRENT_PASSWORD_FIELD = (By.XPATH, '//label[contains(string(), "Current password")]/..//input')
    NEW_PASSWORD_FIELD = (By.XPATH, '//label[contains(string(), "New password")]/..//input')
    SAVE_CHANGES_BUTTON = (By.XPATH, '//button[contains(string(), "Save changes")]/div')
    DISABLED_SAVE_CHANGES_BUTTON = (By.XPATH, '//button[contains(@class, "Disabled")]/div')
    FIRST_NAME_FIELD_ERROR_NOTIFICATION = (By.XPATH, '//label[contains(string(), "First name")]/..//span/span')
    LAST_NAME_FIELD_ERROR_NOTIFICATION = (By.XPATH, '//label[contains(string(), "Last name")]/..//span/span')
    NEW_PASSWORD_FIELD_ERROR_NOTIFICATION = (By.XPATH, '//label[contains(string(), "Current password")]/..//span/span')
    CURRENT_PASSWORD_FIELD_ERROR_NOTIFICATION = (By.XPATH, '//label[contains(string(), "New password")]/..//span/span')
    NOTIFICATION_ERROR = (By.XPATH, '//p')
