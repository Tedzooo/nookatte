from os import *
from urllib.parse import *
from pyrogram.types import *
from pyrogram import *
Pyrogrambot = Client(
    "Pyrogram Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    plugins=dict(root="pyrogrambot")
)
@pr0fess0r_99.on_message(filters.private & filters.text & ~filters.command(["start"]))
async def sharelink(bot, update):
    await bot.send_photo(chat_id=update.chat.id, photo=environ.get("BOT_PIC", "https://telegra.ph/file/2b82d3a491f6b5869092c.jpg"),
        caption=f"**Message Sharing Link Is Ready** :- https://t.me/share/url?url={quote(update.text)}", reply_to_message_id=update.id, reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("📤 Share Link 📤", url=f"https://t.me/share/url?url={quote(update.text)}") ]] )       
    )

Pyrogrambot.run()
