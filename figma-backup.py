#encoding: utf-8
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import TimeoutException

import time

def _timestamp():
	myTime = time.strftime('%Y-%m-%d %H:%M:%S')
	print(myTime)

print('Start:' + str(_timestamp()))

baseURL = "https://www.figma.com"
loginURL = "https://www.figma.com/login"
driverTimeout = 20

#driver = webdriver.Firefox() 

# Headless
# from selenium.webdriver.firefox.options import Options
options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=options, executable_path="C:\\Users\\kgs-adi.azman\\Desktop\\python\\bin\\geckodriver.exe")

print('Firefox:' + str(_timestamp()))

driver.get(loginURL)

print('Page:' + str(_timestamp()))

userId = ''
userPwd = ''

def login():
    driver.find_element_by_xpath('//input[contains(@name, "email")]').send_keys(userId)
    driver.find_element_by_xpath('//input[contains(@name, "password")]').send_keys(userPwd)
    driver.find_element_by_xpath('//button[text()="Sign in"]').click()

login()
print('Login:' + str(_timestamp()))

print(driver.find_element_by_tag_name('body').size)
print('Dashboard:' + str(_timestamp()))

driver.close()

print('Closed:' + str(_timestamp()))

# driver.find_element_by_tag_name('div').text()

# driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))

# list all elements
# driver.find_elements_by_xpath("//*[not(*)]")
# list all elements
# for elm in driver.find_elements_by_xpath("//*[not(*)]"):
#     if elm.tag_name == "div":
#         print(elm.text)



# wait = WebDriverWait(driver, 100)

# driver.find_element_by_xpath('//a[text()="Sign In"]').click()

#wait.until(EC.presence_of_element_located((By.TAG_NAME, 'input')))

# for elm in driver.find_elements_by_tag_name('div'):
#     print(elm.text)
