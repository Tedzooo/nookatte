from pyrogram import Client, filters
from pyrogrambot.photos import PHOTOS
from pyrogrambot.buttons import button
from pyrogram.types import ReplyKeyboardMarkup 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant 
import random
import asyncio
import pytz, datetime
FORCE_SUB = "tzobotz"


@Client.on_message(filters.command("start")) 
async def start_message(bot, message):
    m = datetime.datetime.now(pytz.timezone("Asia/Kolkata"))
    time = m.hour

    if time < 12:
        get="Gᴏᴏᴅ Mᴏʀɴɪɴɢ"
    elif time < 15:
        get="Gᴏᴏᴅ Aғᴛᴇʀɴᴏᴏɴ"
    elif time < 20:
        get="Gᴏᴏᴅ Eᴠᴇɴɪɴɢ"
    else:
        get="Gᴏᴏᴅ Nɪɢʜᴛ"
    await message.reply_photo(
        photo=random.choice(PHOTOS),
        caption=f"""<b>{get} 👋, {message.from_user.mention}
Tʜɪs Is A Pʏʀᴏɢʀᴀᴍ Bᴏᴛ Cʀᴇᴀᴛᴇᴅ Bʏ [Tʜɪs Gᴜʏ](https://t.me/tedzo01)
Cʟɪᴄᴋ Bᴇʟᴏᴡ Bᴜᴛᴛᴏɴ Tᴏ Sᴇᴇ Mᴏʀᴇ</b>""",
        reply_markup=ReplyKeyboardMarkup(
                     [[ 
                         "START","HELP","👀"
                     ]]
                )
            )
@Client.on_message(filters.group & filters.command("id")) 
async def id_message(bot, msg):
    text = f"""Tɪᴛʟᴇ : {msg.chat.title}
Usᴇʀɴᴀᴍᴇ : @{msg.chat.username}
Cʜᴀᴛ ɪᴅ : `{msg.chat.id}`
Usᴇʀ ɪᴅ : `{msg.from_user.id}`"""
    await msg.reply_text(text=text)
