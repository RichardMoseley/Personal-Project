import os
import time
import pymongo
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

price_dict = {'index': [], 'div': []}

url = "https://webscraper.io/test-sites/e-commerce/allinone/phones/touch"
browser.visit(url)
time.sleep(1)

html = browser.html
soup = BeautifulSoup(html, "html.parser")

test = soup.findAll('div')
index = 1
for i in test:
    price_dict['index'].append(index)
    price_dict['div'].append(i)
    index += 1
print(price_dict['index'])
test_list = []
for i in price_dict['div']:
    if 'data-commodity' is in i:

        # Quit the browser
browser.quit()
