import time
import requests
import bs4
import lxml
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from os import system
import re

def EVGA():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://eu.evga.com/products/product.aspx?pn=10G-P5-3881-KR")
    #driver.find_element_by_id("offersofproduct").send_keys(Keys.F5)

    content = driver.page_source.encode('utf-8').strip()
    soup = bs4.BeautifulSoup(content, "html.parser")

    titel = soup.find('h1', attrs={'class', 'product-name'})
    preis = soup.find('span', attrs={'class', 'price'})

    print(titel.text)
    print(preis.text)

    driver.close()
