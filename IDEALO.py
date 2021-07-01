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

def IDEALO():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.idealo.it/confronta-prezzi/200628360/pny-geforce-rtx-3080.html")
    #driver.find_element_by_id("offersofproduct").send_keys(Keys.F5)

    content = driver.page_source.encode('utf-8').strip()
    soup = bs4.BeautifulSoup(content, "html.parser")

    titel = soup.find('h1', attrs={'class', 'oopStage-title'})
    preis = soup.find('span', attrs={'class', 'table-cell oopStage-priceRangePrice'})

    print(titel.text)
    print(preis.text)

    driver.close()
