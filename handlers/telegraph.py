import os
from telegraph import upload_file
import pyrogram
from pyrogram import filters, Client
from config import *
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent,InlineKeyboardMarkup, InlineKeyboardButton,CallbackQuery, InlineQuery


DARK = Client(
   "DARKS PM CHAT",
   api_id=config.APP_ID,
   api_hash=config.API_HASH,
   bot_token=config.BOT_TOKEN,
)

@DARK.on_message(filters.photo & filters.incoming & filters.command("tgp"))
async def uploadphoto(client, message):
  msg = await message.reply_text("∂σωηℓσα∂ιηg❍❍❍❍❍")
  userid = str(message.chat.id)
  img_path = (f"./DOWNLOADS/{userid}.jpg")
  img_path = await client.download_media(message=message, file_name=img_path)
  await msg.edit_text("∂σωηℓσα∂ιηg◉❍❍❍❍")
  await msg.edit_text("∂σωηℓσα∂ιηg◉◉❍❍❍")
  await msg.edit_text("∂σωηℓσα∂ιηg◉◉◉❍❍")
  await msg.edit_text("∂σωηℓσα∂ιηg◉◉◉◉❍")
  await msg.edit_text("∂σωηℓσα∂ιηg◉◉◉◉◉")
  await msg.edit_text("▓▒▒▒▒▒▒▒▒▒▒▒▒")
  await msg.edit_text("▓▓▒▒▒▒▒▒▒▒▒▒▒")
  await msg.edit_text("▓▓▓▒▒▒▒▒▒▒▒▒▒")
  await msg.edit_text("▓▓▓▓▒▒▒▒▒▒▒▒▒")
  await msg.edit_text("▓▓▓▓▓▒▒▒▒▒▒▒▒")
  await msg.edit_text("▓▓▓▓▓▓▒▒▒▒▒▒▒")
  await msg.edit_text("▓▓▓▓▓▓▓▒▒▒▒▒▒")
  await msg.edit_text("▓▓▓▓▓▓▓▓▒▒▒▒▒")
  await msg.edit_text("▓▓▓▓▓▓▓▓▓▒▒▒▒")
  await msg.edit_text("▓▓▓▓▓▓▓▓▓▓▒▒▒")
  await msg.edit_text("▓▓▓▓▓▓▓▓▓▓▓▒▒")
  await msg.edit_text("▓▓▓▓▓▓▓▓▓▓▓▓▒")
  await msg.edit_text("▓▓▓▓▓▓▓▓▓▓▓▓▓")  
  await msg.edit_text("υ❍❍❍❍❍`")
  await msg.edit_text("υρ❍❍❍❍❍")
  await msg.edit_text("υρℓ❍❍❍❍❍")
  await msg.edit_text("υρℓσ❍❍❍❍❍")
  await msg.edit_text("υρℓσα❍❍❍❍❍")
  await msg.edit_text("υρℓσα∂❍❍❍❍❍")
  await msg.edit_text("υρℓσα∂ι❍❍❍❍❍")
  await msg.edit_text("υρℓσα∂ιn❍❍❍❍❍")
  await msg.edit_text("υρℓσα∂ιng❍❍❍❍❍")
  await msg.edit_text("υρℓσα∂ιng◉❍❍❍❍")
  await msg.edit_text("υρℓσα∂ιng◉◉❍❍❍")
  await msg.edit_text("υρℓσα∂ιng◉◉◉❍❍")
  await msg.edit_text("υρℓσα∂ιng◉◉◉◉❍")
  await msg.edit_text("υρℓσα∂ιng◉◉◉◉◉")   
  try:
    tlink = upload_file(img_path)
  except:
    await msg.edit_text("`Something went wrong`") 
  else:
    await msg.edit_text(f"https://telegra.ph{tlink[0]}")     
    os.remove(img_path) 

@DARK.on_message(filters.animation & filters.incoming & filters.command("tga"))
async def uploadgif(client, message):
  if(message.animation.file_size < 5242880):
    msg = await message.reply_text("∂σωηℓσα∂ιηg❍❍❍❍❍")
    userid = str(message.chat.id)
    gif_path = (f"./DOWNLOADS/{userid}.mp4")
    gif_path = await client.download_media(message=message, file_name=gif_path)
  await msg.edit_text("∂σωηℓσα∂ιηg◉❍❍❍❍")
  await msg.edit_text("∂σωηℓσα∂ιηg◉◉❍❍❍")
  await msg.edit_text("∂σωηℓσα∂ιηg◉◉◉❍❍")
  await msg.edit_text("∂σωηℓσα∂ιηg◉◉◉◉❍")
  await msg.edit_text("∂σωηℓσα∂ιηg◉◉◉◉◉")
  await msg.edit_text("▓▒▒▒▒▒▒▒▒▒▒▒▒")
  await msg.edit_text("▓▓▒▒▒▒▒▒▒▒▒▒▒")
  await msg.edit_text("▓▓▓▒▒▒▒▒▒▒▒▒▒")
  await msg.edit_text("▓▓▓▓▒▒▒▒▒▒▒▒▒")
  await msg.edit_text("▓▓▓▓▓▒▒▒▒▒▒▒▒")
  await msg.edit_text("▓▓▓▓▓▓▒▒▒▒▒▒▒")
  await msg.edit_text("▓▓▓▓▓▓▓▒▒▒▒▒▒")
  await msg.edit_text("▓▓▓▓▓▓▓▓▒▒▒▒▒")
  await msg.edit_text("▓▓▓▓▓▓▓▓▓▒▒▒▒")
  await msg.edit_text("▓▓▓▓▓▓▓▓▓▓▒▒▒")
  await msg.edit_text("▓▓▓▓▓▓▓▓▓▓▓▒▒")
  await msg.edit_text("▓▓▓▓▓▓▓▓▓▓▓▓▒")
  await msg.edit_text("▓▓▓▓▓▓▓▓▓▓▓▓▓")  
  await msg.edit_text("υ❍❍❍❍❍`")
  await msg.edit_text("υρ❍❍❍❍❍")
  await msg.edit_text("υρℓ❍❍❍❍❍")
  await msg.edit_text("υρℓσ❍❍❍❍❍")
  await msg.edit_text("υρℓσα❍❍❍❍❍")
  await msg.edit_text("υρℓσα∂❍❍❍❍❍")
  await msg.edit_text("υρℓσα∂ι❍❍❍❍❍")
  await msg.edit_text("υρℓσα∂ιn❍❍❍❍❍")
  await msg.edit_text("υρℓσα∂ιng❍❍❍❍❍")
  await msg.edit_text("υρℓσα∂ιng◉❍❍❍❍")
  await msg.edit_text("υρℓσα∂ιng◉◉❍❍❍")
  await msg.edit_text("υρℓσα∂ιng◉◉◉❍❍")
  await msg.edit_text("υρℓσα∂ιng◉◉◉◉❍")
  await msg.edit_text("υρℓσα∂ιng◉◉◉◉◉")   
    try:
      tlink = upload_file(gif_path)
      await msg.edit_text(f"https://telegra.ph{tlink[0]}")   
      os.remove(gif_path)   
    except:
      await msg.edit_text("Something really Happend Wrong...") 
  else:
    await message.reply_text("Size Should Be Less Than 5 mb")

@DARK.on_message(filters.video & filters.incoming & filters.command("tgv"))
async def uploadvid(client, message):
  if(message.video.file_size < 5242880):
    msg = await message.reply_text("∂σωηℓσα∂ιηg❍❍❍❍❍")
    userid = str(message.chat.id)
    vid_path = (f"./DOWNLOADS/{userid}.mp4")
    vid_path = await client.download_media(message=message, file_name=vid_path)
  await msg.edit_text("∂σωηℓσα∂ιηg◉❍❍❍❍")
  await msg.edit_text("∂σωηℓσα∂ιηg◉◉❍❍❍")
  await msg.edit_text("∂σωηℓσα∂ιηg◉◉◉❍❍")
  await msg.edit_text("∂σωηℓσα∂ιηg◉◉◉◉❍")
  await msg.edit_text("∂σωηℓσα∂ιηg◉◉◉◉◉")
  await msg.edit_text("▓▒▒▒▒▒▒▒▒▒▒▒▒")
  await msg.edit_text("▓▓▒▒▒▒▒▒▒▒▒▒▒")
  await msg.edit_text("▓▓▓▒▒▒▒▒▒▒▒▒▒")
  await msg.edit_text("▓▓▓▓▒▒▒▒▒▒▒▒▒")
  await msg.edit_text("▓▓▓▓▓▒▒▒▒▒▒▒▒")
  await msg.edit_text("▓▓▓▓▓▓▒▒▒▒▒▒▒")
  await msg.edit_text("▓▓▓▓▓▓▓▒▒▒▒▒▒")
  await msg.edit_text("▓▓▓▓▓▓▓▓▒▒▒▒▒")
  await msg.edit_text("▓▓▓▓▓▓▓▓▓▒▒▒▒")
  await msg.edit_text("▓▓▓▓▓▓▓▓▓▓▒▒▒")
  await msg.edit_text("▓▓▓▓▓▓▓▓▓▓▓▒▒")
  await msg.edit_text("▓▓▓▓▓▓▓▓▓▓▓▓▒")
  await msg.edit_text("▓▓▓▓▓▓▓▓▓▓▓▓▓")  
  await msg.edit_text("υ❍❍❍❍❍`")
  await msg.edit_text("υρ❍❍❍❍❍")
  await msg.edit_text("υρℓ❍❍❍❍❍")
  await msg.edit_text("υρℓσ❍❍❍❍❍")
  await msg.edit_text("υρℓσα❍❍❍❍❍")
  await msg.edit_text("υρℓσα∂❍❍❍❍❍")
  await msg.edit_text("υρℓσα∂ι❍❍❍❍❍")
  await msg.edit_text("υρℓσα∂ιn❍❍❍❍❍")
  await msg.edit_text("υρℓσα∂ιng❍❍❍❍❍")
  await msg.edit_text("υρℓσα∂ιng◉❍❍❍❍")
  await msg.edit_text("υρℓσα∂ιng◉◉❍❍❍")
  await msg.edit_text("υρℓσα∂ιng◉◉◉❍❍")
  await msg.edit_text("υρℓσα∂ιng◉◉◉◉❍")
  await msg.edit_text("υρℓσα∂ιng◉◉◉◉◉")   
    try:
      tlink = upload_file(vid_path)
      await msg.edit_text(f"https://telegra.ph{tlink[0]}")     
      os.remove(vid_path)   
    except:
      await msg.edit_text("Something really Happend Wrong...") 
  else:
    await message.reply_text("Size Should Be Less Than 5 
