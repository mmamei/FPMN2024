from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from secret import key
from utils import *


async def process_location(update, context):
    if update.edited_message:
        message = update.edited_message
    else:
        message = update.message
    user_location = message.location

    user = message.from_user
    lat = user_location.latitude
    lon = user_location.longitude
    r = search(restaurants,lat,lon)
    msg = "\n".join([f"{x['name']} - {crea_link_google_maps(x['lat'],x['lon'])}" for x in r])
    await message.reply_text(msg)

print('starting')
restaurants = parseData()
app = ApplicationBuilder().token(key).build()
app.add_handler(MessageHandler(filters.LOCATION, process_location))
app.run_polling()