""" Hack Animation """"

# Copyright (C)

from pyrogram.enums import ParseMode
from pyrogram import Client, filters
import random
import asyncio

# Define a function to handle the /start command
@app.on_message(filters.command("start"))
async def hak(client: Client, message: Message):
    await message.edit_text("Looking for WhatsApp databases in targeted person...")
    await asyncio.sleep(2)
    await message.edit_text(
        " User online: True\nTelegram access: True\nRead Storage: True "
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "Hacking... 0%\n[░░░░░░░░░░░░░░░░░░░░]\n`Looking for WhatsApp...`\nETA: 0m, 20s"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "Hacking... 11.07%\n[██░░░░░░░░░░░░░░░░░░]\n`Looking for WhatsApp...`\nETA: 0m, 18s"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "Hacking... 20.63%\n[███░░░░░░░░░░░░░░░░░]\n`Found folder C:/WhatsApp`\nETA: 0m, 16s"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "Hacking... 34.42%\n[█████░░░░░░░░░░░░░░░]\n`Found folder C:/WhatsApp`\nETA: 0m, 14s"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "Hacking... 42.17%\n[███████░░░░░░░░░░░░░]\n`Searching for databases`\nETA: 0m, 12s"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "Hacking... 55.30%\n[█████████░░░░░░░░░░░]\n`Found msgstore.db.crypt12`\nETA: 0m, 10s"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "Hacking... 64.86%\n[███████████░░░░░░░░░]\n`Found msgstore.db.crypt12`\nETA: 0m, 08s"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "Hacking... 74.02%\n[█████████████░░░░░░░]\n`Trying to Decrypt...`\nETA: 0m, 06s"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "Hacking... 86.21%\n[███████████████░░░░░]\n`Trying to Decrypt...`\nETA: 0m, 04s"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "Hacking... 93.50%\n[█████████████████░░░]\n`Decryption successful!`\nETA: 0m, 02s"
    )
    await asyncio.sleep(2)
    await message.edit_text(
        "Hacking... 100%\n[████████████████████]\n`Scanning file...`\nETA: 0m, 00s"
    )
    await asyncio.sleep(2)
    await message.edit_text("Hacking complete!\nUploading file...")
    await asyncio.sleep(2)
    await message.edit_text(
        "Targeted Account Hacked...!\n\n ✅ File has been successfully uploaded to my server.\nWhatsApp Database:\n`./DOWNLOADS/msgstore.db.crypt12`"
    )
    


"""@Client.on_cmd("hack$", about={"header": "kensar hacking animation"})
async def hack_func(message):
    user = await message.client.get_user_dict(message.from_user.id)
    heckerman = user["mention"]
    animation_chars = [
        "<pre>Connecting To Private Server \\</pre>",
        "<pre>Connecting To Private Server |</pre>",
        "<pre>Connecting To Private Server /</pre>",
        "<pre>Connecting To Private Server \\</pre>",
        "<pre>Connection Established </pre>",
        "<pre>Target Selected</pre>",
        "<pre>Backdoor Found In Target</pre>",
        "<pre>Trying To Hack</pre>",
        "<pre>Hacking... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒</pre>",
        "<pre>Hacking... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒</pre>",
        "<pre>Hacking... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒</pre>",
        "<pre>Hacking... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒</pre>",
        "<pre>Hacking... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒</pre>",
        "<pre>Hacking... 52%\n█████████████▒▒▒▒▒▒▒▒▒</pre>",
        "<pre>Hacking... 70%\n█████████████████▒▒▒▒▒</pre>",
        "<pre>Hacking... 88%\n█████████████████████▒</pre>",
        "<pre>Hacking... 100%\n███████████████████████</pre>",
        "<pre>Preparing Data... 1%\n▒██████████████████████</pre>",
        "<pre>Preparing Data... 14%\n████▒██████████████████</pre>",
        "<pre>Preparing Data... 30%\n████████▒██████████████</pre>",
        "<pre>Preparing Data... 55%\n████████████▒██████████</pre>",
        "<pre>Preparing Data... 72%\n████████████████▒██████</pre>",
        "<pre>Preparing Data... 88%\n████████████████████▒██</pre>",
        "<pre>Prepared Data... 100%\n███████████████████████</pre>",
        "<pre>Uploading Data to Server... 12%\n███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒</pre>",
        "<pre>Uploading Data to Server... 44%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒</pre>",
        "<pre>Uploading Data to Server... 68%\n███████████████▒▒▒▒▒▒▒▒</pre>",
        "<pre>Uploading Data to Server... 89%\n████████████████████▒▒▒</pre>",
        "<pre>Uploaded Data to Server... 100%\n███████████████████████</pre>",
        "<b>User Data Upload Completed:</b> Target's User Data Stored "
        "at <code>downloads/victim/telegram-authuser.data.sql</code>",
    ]
    hecked = (
        f"<b>Targeted Account Hacked</b>\n\n<pre>Pay 69$ To</pre> {heckerman}<pre> "
        "To Remove This Hack</pre>"
    )
    max_ani = len(animation_chars)
    for i in range(max_ani):
        await asyncio.sleep(2)
        await message.edit(animation_chars[i % max_ani], parse_mode=ParseMode.HTML)
    await message.edit(hecked, parse_mode=ParseMode.HTML)"""
