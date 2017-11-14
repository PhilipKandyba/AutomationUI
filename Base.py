import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class Page:

    def __init__(self, driver):
        self.driver = driver
        driver.maximize_window()

    def find_element(self, locator):
        return self.driver.find_element(locator[0], locator[1])

    def is_displayed(self, locator):
        print('base.is_displayed')
        result = self.driver.find_element(locator[0], locator[1]).is_displayed()
        print(result)
        return self.driver.find_element(locator[0], locator[1]).is_displayed()

    def send_keys(self, locator, text):
        self.driver.find_element(locator[0], locator[1]).clear()
        self.driver.find_element(locator[0], locator[1]).send_keys(text)

    def open_page(self, url):
        self.driver.get(url)

    def click(self, locator):
        self.driver.find_element(locator[0], locator[1]).click()

    def wait(self, locator):
        WebDriverWait(self.driver, 100).until(ec.visibility_of_element_located(locator))

    def get_text(self, locator):
        return self.driver.find_element(locator[0], locator[1]).text


