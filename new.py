from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://client.triggmine.com.ua/login')

# assert driver.find_element_by_xpath('//span').text == 'Required'
driver.find_element_by_xpath('//*[@type="email"]').send_keys('qwe_qwe@qwe.com')
driver.find_element_by_xpath('//*[@type="password"]').send_keys('123456')
driver.find_element_by_xpath('//button').click()
time.sleep(1.5)
assert driver.find_element_by_xpath('//p').is_displayed()
assert driver.find_element_by_xpath('//p').
driver.quit()