import requests
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from Data.URL import base_page


class Page:
    def __init__(self, driver):
        self.driver = driver
        driver.maximize_window()

    def find_element(self, locator):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(locator[0], locator[1])

    def is_displayed(self, locator):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(locator[0], locator[1]).is_displayed()

    def send_keys(self, locator, text):
        self.driver.find_element(locator[0], locator[1]).clear()
        self.driver.find_element(locator[0], locator[1]).send_keys(text)

    def open_page(self, url):
        response = requests.get(base_page + url)
        if response.status_code != 200:
            raise Exception('Page is not available, status code: ' + str(response.status_code))
        else:
            self.driver.get(base_page + url)

    def click(self, locator):
        WebDriverWait(self.driver, 100).until(ec.visibility_of_element_located((locator[0], locator[1]))).click()

    def wait(self, locator):
        WebDriverWait(self.driver, 100).until(ec.visibility_of_element_located(locator))

    def get_text(self, locator):
        return self.driver.find_element(locator[0], locator[1]).text


