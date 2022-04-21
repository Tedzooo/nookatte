from pyrogram import Client
import os

Pyrogrambot = Client(
    "Pyrogram Bot",
    bot_token = os.environ["5308384451:AAHZvyBujHTTjHMUcuFmB63_fKtsHa2pTv4"],
    api_id = int(os.environ["10325655"]),
    api_hash = os.environ["77c9c6a5df1464c60a95eeb0dadae7c5"],
    plugins=dict(root="pyrogrambot")
)

Pyrogrambot.run()
