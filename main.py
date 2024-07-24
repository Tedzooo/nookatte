from pyrogram import Client
import os

Pyrogrambot = Client(
    "Pyrogram Bot",
    bot_token = os.environ["7384862816:AAHUwGihYbI63mDdMSFR78H6qB8LIpMzLXw"],
    api_id = int(os.environ["15453419"]),
    api_hash = os.environ["6c9c9e5a2e65daf192e7dd9dde026f45"],
    plugins=dict(root="pyrogrambot")
)

Pyrogrambot.run()
