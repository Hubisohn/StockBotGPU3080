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


def Nvidia():
    time.sleep(2)
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://shop.nvidia.com/de-de/geforce/store/gpu/?page=1&limit=9&locale=de-de&category=GPU&gpu=RTX%203080%20Ti,RTX%203080")
    #driver.find_element_by_id("offersofproduct").send_keys(Keys.F5)

    content = driver.page_source.encode('utf-8').strip()
    soup = bs4.BeautifulSoup(content, "html.parser")

    info = soup.find('div', attrs={'class', 'buy'})

    print(info)

    driver.close()
