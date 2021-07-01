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
while True:
#def StockX():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://stockx.com/it-it/nvidia-evga-geforce-rtx-3080-xc3-graphics-card-10g-p5-3885-kr")
    #driver.find_element_by_id("offersofproduct").send_keys(Keys.F5)

    content = driver.page_source.encode('utf-8').strip()
    soup = bs4.BeautifulSoup(content, "html.parser")

    titel = soup.find('h1', attrs={'class': 'name'})
    preis = soup.find('div', attrs={'class': 'sale-value'})
    verfug = soup.find('div', attrs={'class': 'inner'})

    print("StockX")
    print("https://stockx.com/it-it/nvidia-evga-geforce-rtx-3080-xc3-graphics-card-10g-p5-3885-kr")
    print(titel.text)
    print(preis.text)
    print(verfug.text)

    driver.close()