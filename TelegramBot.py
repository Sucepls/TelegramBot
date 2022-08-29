from telegram.ext import *

import requests
import json

APIKEY = '5300118748:AAFSwWl0OpbeoYYdjUSJriXEnS08kG8-cPQ'

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " --" +  json_data[0]['a']
    print(quote)
    return quote



def start_command(update, context):
    return update.message.reply_text("hello!\n i will send you a quote evryday at 12 till you die :D!!!")

def help_command(update,context):
    return update.message.reply_text("And what?\n need to call your mommy?")

def message(update, context):
    txt = str(update.message.text).lower()
    if txt in ("motivational", "انگیزشی"):
        res = get_quote()
    else:
        res = "کصشر ننویس"

    update.message.reply_text(res)

updater = Updater(APIKEY, use_context=True)

dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start_command))
dp.add_handler(CommandHandler("help", help_command))
dp.add_handler(MessageHandler(Filters.text, message))

updater.start_polling(2)
updater.idle()