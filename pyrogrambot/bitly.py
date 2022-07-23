from pyrogram import Client, filters
import requests 
import json 
import os
 
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
