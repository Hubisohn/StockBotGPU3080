import bs4
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from os import system
from colorama import Fore, Back, Style
from telegram.ext import *


def Mediaworld(update, context):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.mediaworld.it/product/p-140082/asus-tuf-geforce-rtx-3080-10gb")

    content = driver.page_source.encode('utf-8').strip()
    soup = bs4.BeautifulSoup(content, "html.parser")

    titel = soup.find('h1', attrs={'class', 'product-name hidden-xs'})
    preis = soup.find('span', attrs={'class', 'price mw-price enhanced'})

    try:
        inStock = soup.find('p', attrs={'class', 'services__item'}).text
        inStock = str(inStock)
    except NoSuchElementException:
        inStock = "Not Available!"


    print("Mediaworld: Message was sent!")

    update.message.reply_text("Mediaworld\n"
                              f"\n"
                              f"{titel.text}"
                              f"\n"
                              f"\n"
                              f"{preis.text}€"
                              f"\n"
                              f"\n"
                              f"{inStock}"
                              f"\n"
                              f"\n"
                              "https://www.mediaworld.it/product/p-140082/asus-tuf-geforce-rtx-3080-10gb")

    driver.close()