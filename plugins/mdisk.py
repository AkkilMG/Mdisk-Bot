# (c) HeimanPictures

import os
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

from config import Config

from mdisk import Mdisk

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.regex('http') & filters.private)
async def remote_upload(bot, message):
    await message.reply_chat_action("typing")
    d = Mdisk(Config.API_KEY)
    link = message.message
    if 'mypowerdisk.com/mybox' in link:
        upload = d.upload(link)
        url = upload
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
