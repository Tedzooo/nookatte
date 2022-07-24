from urllib.parse import *
from pyrogram import Client, filters
from pyrogram.types import *
from pyrogram import *

@Client.on_message(filters.private & filters.command(["linkt"]))
async def sharelink(bot, update):
       if len(update.command) != 2:
        return await update.reply("**--Use Correct Format-- :-\n  • `/share your text`**")
    await update.reply(
        text=f"**Message Sharing Link Is Ready** :- https://t.me/share/url?url={quote(update.text)}", reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("📤 Share Link 📤", url=f"https://t.me/share/url?url={quote(update.text)}") ]] )       
    )
