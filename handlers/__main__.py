
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from handlers.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from handlers import Client as app
from handlers import LOGGER

pm_start_text = """
👋 Hey [{}](tg://user?id={}), **I'm DARK's PM Bot**
**Now send me the song name you want to download**
     
Syntax : ```/song Faded```
      
Powerd By @SL_BOTS_TM 🔥
"""

@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                     InlineKeyboardButton(
                        text="Channel 🙋‍♀️", url="https://t.me/SLBotOfficial"
                    ),
                    InlineKeyboardButton(
                        text="Dev 🔥", url="https://t.me/ImDark_Empire"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)


app.start()
LOGGER.info("""
   ___  ___   ___  __ ______  ___  __  ___  ___  ____  ______
  / _ \/ _ | / _ \/ //_/ __/ / _ \/  |/  / / _ )/ __ \/_  __/
 / // / __ |/ , _/ ,< _\ \  / ___/ /|_/ / / _  / /_/ / / /   
/____/_/ |_/_/|_/_/|_/___/ /_/  /_/  /_/ /____/\____/ /_/    DARKSPM is online.""")

idle()
