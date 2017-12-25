from selenium.webdriver.common.by import By


class SignUpSuccessPageLocators(object):
    HEADER = (By.XPATH, '//h1[contains(string(), "Welcome on board!")]')
    RESEND_BUTTON = (By.XPATH, '//a[contains(string(), "Resend")]')


class SignUpConfirmPageLocators(object):
    HEADER = (By.XPATH, '//h1[contains(string(), "Email successfully verified")]')
    GO_TO_ACCOUNT_BUTTON = (By.XPATH, '//button[contains(string(), "Go to account")]')