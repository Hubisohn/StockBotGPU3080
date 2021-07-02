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
from telegram.ext import *
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def EVGA(update, context):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://eu.evga.com/products/product.aspx?pn=10G-P5-3881-KR")
    #driver.find_element_by_id("offersofproduct").send_keys(Keys.F5)

    content = driver.page_source.encode('utf-8').strip()
    soup = bs4.BeautifulSoup(content, "html.parser")

    titel = soup.find('h1', attrs={'class', 'product-name'})
    preis = soup.find('span', attrs={'class', 'price'})

    print("EVGA: Message was sent!")

    try:
        driver.find_element_by_xpath("/html/body/form/div[3]/div/div/div[3]/div[4]/div[1]/div[2]/div[3]/div/div/div[1]/div[2]/div/a/span")
        verfug = "Verfügbar!"
    except NoSuchElementException:
        verfug = "Nicht verügbar!"

    update.message.reply_text("EVGA\n"
                              f"\n"
                              f"{titel.text}\n"
                              f"\n"
                              f"{preis.text}\n"
                              f"\n"
                              f"\n"
                              f"{verfug}\n"
                              f"\n"
                              f"\n"
                              "https://eu.evga.com/products/product.aspx?pn=10G-P5-3881-KR")

    driver.close()
