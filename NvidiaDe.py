import bs4
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from os import system
from colorama import Fore, Back, Style
from telegram.ext import *


def Nvidia(update, context):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://shop.nvidia.com/de-de/geforce/store/gpu/?page=1&limit=9&locale=de-de&category=GPU&gpu=RTX%203080%20Ti,RTX%203080")

    price = driver.find_element_by_xpath("/html/body/app-root/product/div[1]/div[1]/div[2]/div/featured-product/div/div/div[2]/div[2]/div[1]/div[1]/span[1]")
    afterprice = driver.find_element_by_class_name("decimal")
    inStock = driver.find_element_by_xpath("/html/body/app-root/product/div[1]/div[1]/div[2]/div/featured-product/div/div/div[2]/div[2]/div[1]/div[2]/a")
    title = driver.find_element_by_xpath("/html/body/app-root/product/div[1]/div[1]/div[2]/div/featured-product/div/div/div[2]/div[1]/h2")

    print("Nvidia: Message was sent!")

    update.message.reply_text("NVIDIA\n"
                              f"\n"
                              f"{title.text}"
                              f"\n"
                              f"\n"
                              f"{price.text}{afterprice.text}"
                              f"\n"
                              f"\n"
                              f"{inStock.text}"
                              f"\n"
                              f"\n"
                              "https://shop.nvidia.com/de-de/geforce/store/gpu/?page=1&limit=9&locale=de-de&category=GPU&gpu=RTX%203080%20Ti,RTX%203080")

    driver.close()