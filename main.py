from pyrogram import Client
import os

Pyrogrambot = Client(
    "Pyrogram Bot",
    bot_token = os.environ["5429037260:AAFXhVRUzVpn9X53m2nXMsOcYIL0N_IWO24"],
    api_id = int(os.environ["10325655"]),
    api_hash = os.environ["77c9c6a5df1464c60a95eeb0dadae7c5"],
    plugins=dict(root="pyrogrambot")
)

Pyrogrambot.run()
