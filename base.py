import requests
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from data.url import base_page_test


class Page:
    def __init__(self, driver):
        self.driver = driver
        driver.maximize_window()

    def find_element(self, locator):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(locator[0], locator[1])

    def is_displayed(self, locator):
        self.driver.implicitly_wait(50)
        return self.driver.find_element(locator[0], locator[1]).is_displayed()

    def send_keys(self, locator, text):
        self.driver.find_element(locator[0], locator[1]).clear()
        self.driver.find_element(locator[0], locator[1]).send_keys(text)

    def open_page(self, url):
        base_page = base_page_test
        response = requests.get(base_page + url)
        if response.status_code != 200:
            raise Exception('Page is not available, status code: ' + str(response.status_code))
        else:
            self.driver.get(base_page + url)

    def click(self, locator):
        WebDriverWait(self.driver, 15).until(ec.visibility_of_element_located((locator[0], locator[1]))).click()

    def wait(self, locator):
        WebDriverWait(self.driver, 15).until(ec.visibility_of_element_located(locator))

    def get_text(self, locator):
        return WebDriverWait(self.driver, 15).until(ec.visibility_of_element_located((locator[0], locator[1]))).text

    def open_url(self, url):
        self.driver.get(url)

    def implicitly_wait(self, second):
        self.driver.implicitly_wait(second)

    def switch_to_open_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def current_url(self):
        print(self.driver.current_url)
        return str(self.driver.current_url)
