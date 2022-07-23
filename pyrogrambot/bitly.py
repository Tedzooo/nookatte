from pyrogram import Client, filters
import requests 
import json 
import os
 
@Client.on_message(filters.private & filters.command(['bitly']))
async def start(client,message):
  await message.reply_text(f"Hello {message .from_user.first_name}\ni am bit.ly short link genrator\n made with love by @tedzosir \n send yourl link \n i converte your link", reply_to_message_id = message.message_id)
  
@Client.on_message(filters.private & filters.regex("http|https"))
async def Bitly(client,message):
  URL = message.text
  DOMAIN = "bit.ly"
  value  = {'long_url': URL , 'domain': DOMAIN}
  data = json.dumps(value)
  try:
    r = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers,data = data )
    result = r.json()
    link = result["link"]
    await message.reply_text(f"```{link}```", reply_to_message_id= message.message_id)
  except Exception as e :
    await message.reply_text(e)
