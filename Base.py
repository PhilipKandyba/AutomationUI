import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class Page(object):

    def __init__(self, driver):
        self.driver = driver
        driver.maximize_window()
        driver.get('http://95.67.18.119:4040/login')

    def find_element(self, locator):
        return self.driver.find_element(locator)

    def open_page(self, url):
        self.driver.get(url)

    def click(self):
        self.driver.click()

    def wait(self, xpath, timer=10):
        WebDriverWait(self.driver, timer).until(
            ec.presence_of_element_located((By.XPATH, xpath)))

