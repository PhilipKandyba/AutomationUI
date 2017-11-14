from selenium.webdriver.common.by import By


class SetupPageLocators(object):
    H2_TITLE = (By.XPATH, '//h2[contains(string(), "Coupons & Discount")]')
    TYPE = (By.XPATH, '//*[@name="q"]')
    GOOGLE = (By.XPATH, '//*[@name="btnK"]')
