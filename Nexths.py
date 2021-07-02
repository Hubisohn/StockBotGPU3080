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
from colorama import Fore, Back, Style

def Nexths():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.nexths.it/Products/details/sku/4895173623387")
    #driver.find_element_by_id("offersofproduct").send_keys(Keys.F5)

    content = driver.page_source.encode('utf-8').strip()
    soup = bs4.BeautifulSoup(content, "html.parser")

    titel = soup.find('h1', attrs={'class': 'itempage_title'})
    preis = soup.find('span', attrs={'class': 'prezzo_normale oswald'})
    verfug = soup.find('a', attrs={'class': 'btn btn-success'})

    print(Fore.YELLOW + "Nexths")
    print(Fore.WHITE + "https://www.nexths.it/Products/details/sku/4895173623387")
    print(titel.text)
    print(preis.text)
    print(verfug.text)

    driver.close()