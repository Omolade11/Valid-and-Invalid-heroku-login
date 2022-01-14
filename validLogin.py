import os
from _ast import Assert

from selenium import webdriver
from selenium.webdriver.common.by import By


os.environ['PATH'] += r"/usr/local/bin/chromedriver"
driver = webdriver.Chrome()

driver.maximize_window()
driver.get('https://the-internet.herokuapp.com')
driver.implicitly_wait(10)


driver.find_element(By.LINK_TEXT, "Form Authentication").click()

username = 'tomsmith'
password = 'SuperSecretPassword!'

# login
driver.find_element(By.ID, "username").send_keys(username)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.TAG_NAME, "button").click()


element = driver.find_element(By.ID, 'flash').text()
assert element.text == 'You logged into a secure area!'
