from telegram.ext import *
import time
import sys

import Mediaworldit
import Newegg
import IDEALO
import NvidiaDe
import EVGA
import Nexths

API_KEY = '1640641322:AAFZ08xmXQN7lLNQjPFJ45motnvhC7100gw'

print("Der Bot startet!")

open(r"C:\Users\ManuelU\Desktop\stckbot special items\log.txt", "w")

def send_gpu(update, context):
    while True:
        IDEALO.IDEALO(update, context)
        sys.stdout = open(r"C:\Users\ManuelU\Desktop\stckbot special items\log.txt", "a")
        EVGA.EVGA(update, context)
        sys.stdout = open(r"C:\Users\ManuelU\Desktop\stckbot special items\log.txt", "a")
        NvidiaDe.Nvidia(update, context)
        sys.stdout = open(r"C:\Users\ManuelU\Desktop\stckbot special items\log.txt", "a")
        Nexths.Nexths(update, context)
        sys.stdout = open(r"C:\Users\ManuelU\Desktop\stckbot special items\log.txt", "a")
        Newegg.Newegg(update, context)
        sys.stdout = open(r"C:\Users\ManuelU\Desktop\stckbot special items\log.txt", "a")
        Mediaworldit.Mediaworld(update, context)
        sys.stdout = open(r"C:\Users\ManuelU\Desktop\stckbot special items\log.txt", "a")
        update.message.reply_text("Heibs Maul und loss mi itz fi 15 min penn du fock")
        time.sleep(900)

def main():
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", send_gpu))

    updater.start_polling()
    updater.idle()

    sys.stdout = open(r"C:\Users\ManuelU\Desktop\stckbot special items", "w")

main()