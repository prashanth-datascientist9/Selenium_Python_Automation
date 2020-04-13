import os
import pandas as pd
import ssl
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")
ssl._create_default_https_context = ssl._create_unverified_context

driver = webdriver.Chrome(executable_path = DRIVER_BIN)
driver.implicitly_wait(5)

with open('Eagle_Site_Links_2.txt') as file:
    for line in file:
        print('Link : ' + line)
        outfile = line.split(';')[0]
        url = line.split(';')[1]
        driver.get(url)
        driver.find_element_by_id('tools-menu-trigger').click()
        driver.find_element_by_id('action-view-source-link').click()

        print('Current URL : ' + driver.current_url)
        page = requests.get(driver.current_url)

        soup = BeautifulSoup(page.content, 'html.parser')

        try:
            tbl = soup.find('table', {'class': 'wrapped relative-table confluenceTable'})
            data_frame = pd.read_html(str(tbl))[0]
        except ValueError:
            print('No Table class with "wrapped relative-table confluenceTable" found')
            tbl = soup.find('table', {'class': 'wrapped confluenceTable'})
            data_frame = pd.read_html(str(tbl))[0]

        with pd.ExcelWriter(outfile) as writer:
            data_frame.to_excel(writer, sheet_name='Data Mapping')
    print('Download complete')
    driver.quit()
    file.close()
