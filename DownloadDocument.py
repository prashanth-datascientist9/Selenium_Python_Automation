from selenium import webdriver
import os

url = 'http://www.google.com'
#find_elements_by_xpath('.//span[@class = "gbts"]')
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")

driver = webdriver.Chrome(executable_path = DRIVER_BIN)

driver.get(url)

input('Press ENTER to close the automated browser')

driver.quit()

