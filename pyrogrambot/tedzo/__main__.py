""" Hack Animation """

# Copyright (C)


import asyncio

from pyrogram import Client 
from pyrogram.enums import ParseMode


@Client.on_cmd("hack$", about={"header": "kensar hacking animation"})
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
    await message.edit(hecked, parse_mode=ParseMode.HTML)
