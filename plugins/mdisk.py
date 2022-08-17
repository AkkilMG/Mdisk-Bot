# (c) HeimanPictures

import os
import requests
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

from config import Config

#from mdisk import Mdisk


import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.regex('http') & filters.private)
async def remote_upload(bot, message):
    # await message.reply_chat_action("typing")
    
    link = message.text #.split(' ')[0]
    if ('mypowerdisk.com/mybox' in link) or ('mdisk.me' in link):
        param = {'token':Config.API_KEY, 'link':str(link)} 
        r = requests.post(link, json = param) 
        response = r.json()
        data = dict(response)
        mdisk = data["sharelink"]
        
        url = mdisk
        await message.reply_text(
            text=f"**Video Link:** `{url}`\n\n This Code is made by @HeimanSupports.",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton('Doodstream', url=url)]]
            )
        )
    else:
        await message.reply_text(
            "__I Am Facing Some Issue, Please Check the input link or its way that you have provided and if you feel its an error in code please contact **@HeimanSupport**__"
        )
