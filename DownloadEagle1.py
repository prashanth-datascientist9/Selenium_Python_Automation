import os

from selenium import webdriver

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")

driver = webdriver.Chrome(executable_path = DRIVER_BIN)

with open('Eagle_Site_Links.txt') as file:
    for url in file:
        print('Link : ' + url)
        driver.get(url)
        driver.find_element_by_id('tools-menu-trigger').click()
        driver.find_element_by_id('action-export-word-link').click()
    driver.quit()
    file.close()
