from selenium.webdriver.common.by import By


class DashboardPageLocators(object):
    STATISTIC_HEADER = (By.XPATH, '//h3[1]')
    INTERCOM_IFRAME = (By.XPATH, '//iframe[@class="intercom-launcher-frame"]')
    INTERCOM_OPEN_CHAT_BUTTON = (By.CLASS_NAME, 'intercom-avatar')
    INTERCOM_CHAT = (By.CLASS_NAME, 'intercom-conversations')
    CURRENCY_SYMBOL = (By.XPATH, '//sup')
