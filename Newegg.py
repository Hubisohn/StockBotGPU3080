import bs4
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from os import system
from colorama import Fore, Back, Style
from telegram.ext import *


def Newegg(update, context):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.newegg.com/asus-geforce-rtx-3080-ti-tuf-rtx3080ti-12g-gaming/p/N82E16814126510?nm_mc=AFC-RAN-COM&cm_mmc=AFC-RAN-COM&utm_medium=affiliates&utm_source=afc-Future+Publishing+Ltd&AFFID=2294204&AFFNAME=Future+Publishing+Ltd&ACRID=1&ASUBID=grd-it-1237961056049486300&ASID=https%3A%2F%2Fwww.gamesradar.com%2Fwhere-to-buy-rtx-3080-ti-graphics-cards%2F&ranMID=44583&ranEAID=2294204&ranSiteID=kXQk6.ivFEQ-eiLLpMZWwjLxLWaGLABuDg")

    price = driver.find_element_by_xpath("/html/body/div[6]/div[2]/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/ul/li[3]/strong")
    inStock = driver.find_element_by_xpath("/html/body/div[6]/div[2]/div[1]/div/div/div[1]/div[1]/div[1]/div/div/span")
    title = driver.find_element_by_xpath("/html/body/div[6]/div[2]/div[1]/div/div/div[2]/div[1]/div[5]/h1")

    print("Newegg: Message was sent!")

    update.message.reply_text("Newegg\n"
                              f"\n"
                              f"{title.text}"
                              f"\n"
                              f"\n"
                              f"{price.text}€"
                              f"\n"
                              f"\n"
                              f"{inStock.text}"
                              f"\n"
                              f"\n"
                              "https://www.newegg.com/asus-geforce-rtx-3080-ti-tuf-rtx3080ti-12g-gaming/p/N82E16814126510?nm_mc=AFC-RAN-COM&cm_mmc=AFC-RAN-COM&utm_medium=affiliates&utm_source=afc-Future+Publishing+Ltd&AFFID=2294204&AFFNAME=Future+Publishing+Ltd&ACRID=1&ASUBID=grd-it-1237961056049486300&ASID=https%3A%2F%2Fwww.gamesradar.com%2Fwhere-to-buy-rtx-3080-ti-graphics-cards%2F&ranMID=44583&ranEAID=2294204&ranSiteID=kXQk6.ivFEQ-eiLLpMZWwjLxLWaGLABuDg")

    driver.close()