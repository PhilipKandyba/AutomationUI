import requests
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from data.url import base_page_test


class Page:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        self.driver.find_element(locator[0], locator[1])

    def is_displayed(self, locator):
        return WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located
                                                    ((locator[0], locator[1]))).is_displayed()

    def send_keys(self, locator, text):
        WebDriverWait(self.driver, 15).until(ec.visibility_of_element_located((locator[0], locator[1]))).clear()
        WebDriverWait(self.driver, 15).until(ec.visibility_of_element_located((locator[0], locator[1]))).send_keys(text)

    def open_page(self, url):
        base_page = base_page_test
        response = requests.get(base_page + url)
        if response.status_code != 200:
            raise Exception('Page is not available, status code: ' + str(response.status_code))
        else:
            self.driver.get(base_page + url)

    def click(self, locator):
        WebDriverWait(self.driver, 15).until(ec.element_to_be_clickable((locator[0], locator[1]))).click()

    def wait(self, second, locator):
        WebDriverWait(self.driver, second).until(ec.visibility_of_element_located((locator[0], locator[1])))

    def wait_until_element_is_not_show(self, second, locator):
        WebDriverWait(self.driver, second).until(ec.invisibility_of_element_located((locator[0], locator[1])))

    def get_text(self, locator):
        return WebDriverWait(self.driver, 15).until(ec.visibility_of_element_located((locator[0], locator[1]))).text

    def get_value(self, locator):
        return WebDriverWait(self.driver, 15).until(ec.visibility_of_element_located((
            locator[0], locator[1]))).get_attribute('value')

    def open_url(self, url):
        self.driver.get(url)

    def implicitly_wait(self, second):
        return self.driver.implicitly_wait(second)

    def switch_to_open_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def close_first_windows(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.close()

    def current_url(self):
        for i in range(100):
            page = self.driver.current_url
            if page == 'about:blank':
                import time
                time.sleep(0.05)
                print(i)
                continue
            else:
                break
        response = requests.get(self.driver.current_url)
        if response.status_code != 200:
            raise Exception('Page is not available, status code: ' + str(response.status_code))
        else:
            return page

    def switch_to_frame(self, locator):
        iframe = self.driver.find_element(locator[0], locator[1])
        self.driver.switch_to_frame(iframe)
