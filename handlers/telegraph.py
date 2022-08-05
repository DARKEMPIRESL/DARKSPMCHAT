import os
from telegraph import upload_file
import pyrogram
from pyrogram import filters, Client
from config import *
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent,InlineKeyboardMarkup, InlineKeyboardButton,CallbackQuery, InlineQuery


app = Client(
   "DARKS PM CHAT",
   api_id=API_ID,
   api_hash=API_HASH,
   bot_token=BOT_TOKEN,
)



@app.on_message(filters.command("telegraph"))
async def telegraph(client, message):
    replied = message.reply_to_message
    if not replied:
        await message.reply("Reply to a supported media file")
        return
    if not (
        (replied.photo and replied.photo.file_size <= 5242880)
        or (replied.animation and replied.animation.file_size <= 5242880)
        or (
            replied.video
            and replied.video.file_name.endswith(".mp4")
            and replied.video.file_size <= 5242880
        )
        or (
            replied.document
            and replied.document.file_name.endswith(
                (".jpg", ".jpeg", ".png", ".gif", ".mp4"),
            )
            and replied.document.file_size <= 5242880
        )
    ):
      await message.reply_text("∂σωηℓσα∂ιηg◉❍❍❍❍")
      await message.edit_text("∂σωηℓσα∂ιηg◉◉❍❍❍")
      await message.edit_text("∂σωηℓσα∂ιηg◉◉◉❍❍")
      await message.edit_text("∂σωηℓσα∂ιηg◉◉◉◉❍")
      await message.edit_text("∂σωηℓσα∂ιηg◉◉◉◉◉")
      await message.edit_text("▓▒▒▒▒▒▒▒▒▒▒▒▒")
      await message.edit_text("▓▓▒▒▒▒▒▒▒▒▒▒▒")
      await message.edit_text("▓▓▓▒▒▒▒▒▒▒▒▒▒")
      await message.edit_text("▓▓▓▓▒▒▒▒▒▒▒▒▒")
      await message.edit_text("▓▓▓▓▓▒▒▒▒▒▒▒▒")
      await message.edit_text("▓▓▓▓▓▓▒▒▒▒▒▒▒")
      await message.edit_text("▓▓▓▓▓▓▓▒▒▒▒▒▒")
      await message.edit_text("▓▓▓▓▓▓▓▓▒▒▒▒▒")
      await message.edit_text("▓▓▓▓▓▓▓▓▓▒▒▒▒")
      await message.edit_text("▓▓▓▓▓▓▓▓▓▓▒▒▒")
      await message.edit_text("▓▓▓▓▓▓▓▓▓▓▓▒▒")
      await message.edit_text("▓▓▓▓▓▓▓▓▓▓▓▓▒")
      await message.edit_text("▓▓▓▓▓▓▓▓▓▓▓▓▓")  
      await message.edit_text("υ❍❍❍❍❍`")
      await message.edit_text("υρ❍❍❍❍❍")
      await message.edit_text("υρℓ❍❍❍❍❍")
      await message.edit_text("υρℓσ❍❍❍❍❍")
      await message.edit_text("υρℓσα❍❍❍❍❍")
      await message.edit_text("υρℓσα∂❍❍❍❍❍")
      await message.edit_text("υρℓσα∂ι❍❍❍❍❍")
      await message.edit_text("υρℓσα∂ιn❍❍❍❍❍")
      await message.edit_text("υρℓσα∂ιng❍❍❍❍❍")
      await message.edit_text("υρℓσα∂ιng◉❍❍❍❍")
      await message.edit_text("υρℓσα∂ιng◉◉❍❍❍")
      await message.edit_text("υρℓσα∂ιng◉◉◉❍❍")
      await message.edit_text("υρℓσα∂ιng◉◉◉◉❍")
      await message.edit_text("υρℓσα∂ιng◉◉◉◉◉")   
      await message.reply("Not supported!")
        return
    download_location = await client.download_media(
        message=message.reply_to_message,
        file_name="root/downloads/",
    )
    try:
        response = upload_file(download_location)
    except Exception as document:
        await message.reply(message, text=document)
    else:
        await message.reply_text("∂σωηℓσα∂ιηg◉❍❍❍❍")
        await message.edit_text("∂σωηℓσα∂ιηg◉◉❍❍❍")
        await message.edit_text("∂σωηℓσα∂ιηg◉◉◉❍❍")
        await message.edit_text("∂σωηℓσα∂ιηg◉◉◉◉❍")
        await message.edit_text("∂σωηℓσα∂ιηg◉◉◉◉◉")
        await message.edit_text("▓▒▒▒▒▒▒▒▒▒▒▒▒")
        await message.edit_text("▓▓▒▒▒▒▒▒▒▒▒▒▒")
        await message.edit_text("▓▓▓▒▒▒▒▒▒▒▒▒▒")
        await message.edit_text("▓▓▓▓▒▒▒▒▒▒▒▒▒")
        await message.edit_text("▓▓▓▓▓▒▒▒▒▒▒▒▒")
        await message.edit_text("▓▓▓▓▓▓▒▒▒▒▒▒▒")
        await message.edit_text("▓▓▓▓▓▓▓▒▒▒▒▒▒")
        await message.edit_text("▓▓▓▓▓▓▓▓▒▒▒▒▒")
        await message.edit_text("▓▓▓▓▓▓▓▓▓▒▒▒▒")
        await message.edit_text("▓▓▓▓▓▓▓▓▓▓▒▒▒")
        await message.edit_text("▓▓▓▓▓▓▓▓▓▓▓▒▒")
        await message.edit_text("▓▓▓▓▓▓▓▓▓▓▓▓▒")
        await message.edit_text("▓▓▓▓▓▓▓▓▓▓▓▓▓")  
        await message.edit_text("υ❍❍❍❍❍`")
        await message.edit_text("υρ❍❍❍❍❍")
        await message.edit_text("υρℓ❍❍❍❍❍")
        await message.edit_text("υρℓσ❍❍❍❍❍")
        await message.edit_text("υρℓσα❍❍❍❍❍")
        await message.edit_text("υρℓσα∂❍❍❍❍❍")
        await message.edit_text("υρℓσα∂ι❍❍❍❍❍")
        await message.edit_text("υρℓσα∂ιn❍❍❍❍❍")
        await message.edit_text("υρℓσα∂ιng❍❍❍❍❍")
        await message.edit_text("υρℓσα∂ιng◉❍❍❍❍")
        await message.edit_text("υρℓσα∂ιng◉◉❍❍❍")
        await message.edit_text("υρℓσα∂ιng◉◉◉❍❍")
        await message.edit_text("υρℓσα∂ιng◉◉◉◉❍")
        await message.edit_text("υρℓσα∂ιng◉◉◉◉◉")   
        await message.reply("Not supported!")
        await message.reply(
            f"**Uploaded To Telegraph!\n\n👉 https://telegra.ph{response[0]}**",
            disable_web_page_preview=True,
        )
    finally:
        os.remove(download_location)
