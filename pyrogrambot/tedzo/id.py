from pyrogram import filters
from pyrogram import Client as NaysaBots
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import UserNotParticipant

@NaysaBots.on_message(filters.private & filters.forwarded)
async def info(bot, message):

    if message.forward_from:
        text = "Bot Info 👀 \n\n"
        if message.forward_from["is_bot"]:
            text += "🤖 Forward Info"
        else:
            text += "👤User Info"
        text += f'\n\n👨‍💼 Name : {message.forward_from["first_name"]}'
        if message.forward_from["username"]:
            text += f'\n\n🔗 Username : @{message.forward_from["username"]} \n\n🆔 ID : <code>{message.forward_from["id"]}</code>'
        else:
            text += f'\n\n🆔 ID : `{message.forward_from["id"]}`'
        await message.reply(text, quote=True)
    else:
        hidden = message.forward_sender_name
        if hidden:
            await message.reply(
                f"❌️Error {hidden} ❌️Error",
                quote=True,
            )
        else:
            text = f"Forward Information\n\n"
            if message.forward_from_chat["type"] == "channel":
                text += "📡 Forwarded From Channel"
            if message.forward_from_chat["type"] == "supergroup":
                text += "💬 Group"
            text += f'\n\n📃 Name : `{message.forward_from_chat["title"]}`'
            if message.forward_from_chat["username"]:
                text += f'\n\n📩 From : @{message.forward_from_chat["username"]}'
                text += f'\n\n🆔 ID : `{message.forward_from_chat["id"]}`'
            else:
                text += f'\n\n🆔 ID `{message.forward_from_chat["id"]}`\n\n'
            await message.reply(text, quote=True)
