import os
import random

from pyrogram.errors.exceptions.bad_request_400 import *
from pyrogram.errors import *
from pyrogram import Client, filters
from pyrogram.errors import *
from pyrogram.types import *

#Vars
BOT_TOKEN = os.getenv("BOT_TOKEN", "")  # from @botfather
API_ID = int(os.getenv("API_ID", ""))  # from https://my.telegram.org/apps
API_HASH = os.getenv("API_HASH", "")  # from https://my.telegram.org/apps
MONGO_URI = os.getenv("MONGO_URI", "")
force_subchannel = os.getenv("FSUB", "SLBotOfficial")
OWNER_ID = int(os.environ.get("OWNER_ID", "1120271521"))
START_STRING = os.getenv("START_STRING", "Hi {}, Welcome to  {}'s Pm Bot.")
START_STICKER = os.getenv("START_STICKER", "CAADBQADZQQAAlHy2FQE5VU4XGjXrwI")
DATABASE_URL = os.environ.get('DATABASE_URL', None)
DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
#Strings 
PM_TXT_ATT = "<b>Message from:</b> {}\n<b>Name:</b> {}\n\n{}"
PM_TXT_ATTS = "<b>Message from:</b> {}\n<b>Name:</b> {}"
PM_MED_ATT = "<b>Message from:</b> {} \n<b>Name:</b> {}\n<b>Caption</b>:{}"
FORCESUB_TEXT = "**❌ Access Denied ❌**\n\n♻️Join and Try Again.♻️"
HELP_STRING = """Hello.. I'm 𝕯𝖆𝖗𝖐'𝘀 𝗣𝗠 𝗕𝗼𝘁
Type your query here..
I'll respond to your query as earliest 😉"""



#Inline Btn
FORCESUB_BUTTONS = InlineKeyboardMarkup([[
                 InlineKeyboardButton('Join Here', url=f"https://t.me/{force_subchannel}")
                 ],
                 [
                 InlineKeyboardButton('🐞 ʀᴘᴏʀᴛ ʙᴜɢs 🐞', url="https://t.me/SL_BOTS_TM")
                 ],
                 [
                 InlineKeyboardButton(text="♻️ Reload ♻️",callback_data="ref")
                 ]]
                  )
                  
CLOSE_BUTTON = InlineKeyboardMarkup([[
                 InlineKeyboardButton("𝕮𝖑𝖔𝖒𝖘𝖊", callback_data="cloce")
                 ]]
                 )
                                                    
BACK_BUTTONS = InlineKeyboardMarkup([[
                 InlineKeyboardButton(text="👻 ʙᴀᴍᴄᴋ 👻",callback_data="bak")            
                 ]]
                  ) 

START_BUTTON = InlineKeyboardMarkup([[              
                 InlineKeyboardButton('Team SL Bots🇱🇰', url="https://t.me/SLBotOfficial") , InlineKeyboardButton('┊𝙰𝙻𝙿𝙷𝙰 么 ™ Bots 『🇱🇰』', url="https://t.me/AlphaTm_Botz")
                 ],
                 [
                 InlineKeyboardButton(text="🌴 ʜᴇʟᴘ 🌴",callback_data="hlp")
                 ],
                 [
                 InlineKeyboardButton("🍄 sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ 🍄", url="https://github.com/DARKEMPIRESL/Pm-Chat-bot") 
                 ]]
                  )

DEV_BTN = InlineKeyboardMarkup([[              
            InlineKeyboardButton('𝕯𝖆𝖗𝖐 𝕰𝖒𝖕𝖎𝖗𝖊 🇱🇰🇸 🇱 🇧 🇴 🇹 🇸 ™', user_id="SL_BOTS_TM")
            ],
            [
            InlineKeyboardButton('unknown boy┊𝙰𝙻𝙿𝙷𝙰 么 ™', user_id="UnknownB_o_y")
            ],
            [
            InlineKeyboardButton('ŦħȺɍᵾꝁ ɌɇnᵾɉȺ', user_id="ImTharuk")
            ],
            [
            InlineKeyboardButton('', user_id="ImGishan")
            ],
            [
            InlineKeyboardButton('𝘿𝙚𝙣𝙪𝙬𝙖𝙣 🇱🇰', user_id="ImDenuwan")
            ]]
            )
HELP_BTN = InlineKeyboardMarkup([[              
                 InlineKeyboardButton('Team SL Bots🇱🇰', url="https://t.me/SLBotOfficial") , InlineKeyboardButton('┊𝙰𝙻𝙿𝙷𝙰 么 ™ Bots 『🇱🇰』', url="https://t.me/AlphaTm_Botz")
                 ],
                 [
                 InlineKeyboardButton("🍄 sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ 🍄", url="https://github.com/DARKEMPIRESL/DARKSPMCHAT") 
                 ],
                 [
                 InlineKeyboardButton("Back", callback_data="stback") 
                 ]]
                  )

#Rndm Stkr



STAT_STICKER = ["CAACAgUAAxkBAAIEH2Lh9tYGSUk1wkp8fZEiohjX3S-4AAL_BwACzpT4VHonAgqt8Z-8HgQ",
                "CAACAgUAAxkBAAIEI2Lh9wABwA5eCscl00ee7IQgUeJ8KAACHgUAAqrCAAFVByHxjhsfLyEeBA"              
         ]  

         
DEV_STICKER = ["CAACAgUAAxkBAAIEIWLh9vxLot7QZlvMp1UT_QrX4O92AAJ5BgACNpEBVcaIt8a3oOWLHgQ",
                "CAACAgUAAxkBAAIEJWLh9ylxxyT2oqvRhAQbfn1XGICcAAJxBgAC739QVa3ZGtROSduwHgQ",
                "CAACAgUAAxkBAAIEJ2Lh90I_dTluN575xdOtOgyUmlh6AAJ6CAACffCBVeVVSP1X-RnTHgQ", 
                "CAACAgUAAxkBAAIEKWLh94O2TgqYCzBTjbSXvzAaMnnjAALxBAAC3-zgVH0fBUdAe6TcHgQ",
                "CAACAgUAAxkBAAIEK2Lh954sBHjEbmlYISF8yVDhwgU-AALGCAACdoKAVIudJYK3kEyOHgQ"                
         ] 

HELP_STICKER = ["CAACAgUAAxkBAAIEKWLh94O2TgqYCzBTjbSXvzAaMnnjAALxBAAC3-zgVH0fBUdAe6TcHgQ",
                "CAACAgUAAxkBAAIEK2Lh954sBHjEbmlYISF8yVDhwgU-AALGCAACdoKAVIudJYK3kEyOHgQ",
                "CAACAgUAAxkBAAIELWLh98kRFA4AAfoDGI3S-kuBZVIHXwACnQUAAhFuwVSF2Gck3NMCoB4E", 
                "CAACAgUAAxkBAAIEL2Lh99oeunZQtBSr7O6AMAFCtvNAAAIVBgACp5nAVDHvzXC6IX3UHgQ"               
         ]




print("Config Working....")
