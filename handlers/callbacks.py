from pyrogram import Client
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from handlers.database.chats_sql import Chats, get_action, change_action, get_force_chat, get_ignore_service, toggle_ignore_service, get_only_owner, toggle_only_owner
from handlers.database import SESSION
from pyrogram.errors import UserNotParticipant
import ast
from Data import Data
from handlers.database.whisper_sql import Whispers
from handlers.bot_users import check_for_users
from handlers.admin_check import admin_check
from pyrogram.errors.exceptions import UserNotParticipant
from handlers.start import *
from handlers.calculator import *
from pyrogram.types import *

tick = "✅"
cross = "❌"


# Callbacks
@Client.on_callback_query()
async def _callbacks(bot: Client, callback_query: CallbackQuery):
    user = await bot.get_me()
    mention = user["mention"]
    if callback_query.data.lower() == "supported_media_types":
        chat_id = callback_query.from_user.id
        message_id = callback_query.message.message_id
        await bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=Data.SUPPORTED_MEDIA_TYPES,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(Data.supported_media_buttons),
        )
    elif callback_query.data.lower() == "close":
        chat_id = callback_query.from_user.id
        message_ids = [callback_query.message.message_id, callback_query.message.reply_to_message.message_id]
        await bot.delete_messages(chat_id, message_ids)
    elif callback_query.data.lower() == "everyone":
        user_id = callback_query.from_user.id
        chat_id = callback_query.message.chat.id
        message_id = callback_query.message.message_id
        try:
            chat_user = await bot.get_chat_member(chat_id, user_id)
        except UserNotParticipant:
            return
        if chat_user.status in ["creator", "administrator"]:
            q = SESSION.query(Chats).get(chat_id)
            if q.allow_usage == "Everyone":
                await callback_query.answer("Already set to EVERYONE", show_alert=True)
                SESSION.close()
            else:
                q.allow_usage = "Everyone"
                SESSION.commit()
                await bot.edit_message_reply_markup(
                    chat_id=chat_id,
                    message_id=message_id,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton(f"Allow Usage : Everyone {tick}", callback_data="everyone")],
                        [InlineKeyboardButton(f"Allow Usage : Admins Only {cross}", callback_data="admins_only")]
                    ]),
                )
        else:
            await callback_query.answer("Only admins can change settings.", show_alert=True)
    elif callback_query.data.lower() == "admins_only":
        user_id = callback_query.from_user.id
        chat_id = callback_query.message.chat.id
        message_id = callback_query.message.message_id
        try:
            chat_user = await bot.get_chat_member(chat_id, user_id)
        except UserNotParticipant:
            return
        if chat_user.status in ["creator", "administrator"]:
            q = SESSION.query(Chats).get(chat_id)
            if q.allow_usage == "Admins Only":
                await callback_query.answer("Already set to ADMINS ONLY", show_alert=True)
                SESSION.close()
            else:
                q.allow_usage = "Admins Only"
                SESSION.commit()
                await bot.edit_message_reply_markup(
                    chat_id=chat_id,
                    message_id=message_id,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton(f"Allow Usage : Everyone {cross}", callback_data="everyone")],
                        [InlineKeyboardButton(f"Allow Usage : Admins Only {tick}", callback_data="admins_only")]
                    ]),
                )
        else:
            await callback_query.answer("Only admins can change settings.", show_alert=True)

@Client.on_callback_query()
async def _callbacks(bot, callback_query: CallbackQuery):
	user = await bot.get_me()
	mention = user["mention"]
	if callback_query.data.lower() == "home":
		chat_id = callback_query.from_user.id
		message_id = callback_query.message.message_id
		await bot.edit_message_text(
			chat_id=chat_id,
			message_id=message_id,
			text=Data.START.format(callback_query.from_user.mention, mention),
			reply_markup=InlineKeyboardMarkup(Data.buttons),
		)
	elif callback_query.data.lower() == "about":
		chat_id = callback_query.from_user.id
		message_id = callback_query.message.message_id
		await bot.edit_message_text(
			chat_id=chat_id,
			message_id=message_id,
			text=Data.ABOUT,
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(Data.home_buttons),
		)
	elif callback_query.data.lower() == "help":
		chat_id = callback_query.from_user.id
		message_id = callback_query.message.message_id
		await bot.edit_message_text(
			chat_id=chat_id,
			message_id=message_id,
			text="**Here's How to use me**\n" + Data.HELP,
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(Data.home_buttons),
		)
	else:
		cb_data = callback_query.data
		data_list = ast.literal_eval(str(cb_data))
		if callback_query.from_user.id in data_list:
			specific = callback_query.inline_message_id
			q = SESSION.query(Whispers).get(specific)
			if q:
				await callback_query.answer(q.message, show_alert=True)
			else:
				await callback_query.answer("Message Not Found", show_alert=True)
			SESSION.commit()
		else:
			await callback_query.answer("Sorry, you cannot see this whisper as it is not meant for you!", show_alert=True)
		await check_for_users(data_list)

@Client.on_callback_query()  
async def tgm(bot, update):  
    if update.data == "ref": 
        await update.answer(
             text="♻️Reloading.....♻️",
        )

    elif update.data == "bamk":
         await update.message.edit_text(
             text=START_STRING,
             reply_markup=START_BUTTON,
             disable_web_page_preview=True
         ) 
         await update.answer(
             text="️🍃 𝗕𝗔𝗖𝗞 🍃",
         )
    elif update.data == "tgm":
         await update.message.edit_text(
             text=TELEGRAPH,
             reply_markup=HELPB_BUTTON,
             disable_web_page_preview=True
         )
         await update.answer(
             text="🔱 𝕿𝖊𝖑𝖊𝖌𝖗𝖆𝖕𝖍 🔱",
         )
    elif update.data == "logoc":
         await update.message.edit_text(
             text=LOGO_STRING,
             reply_markup=HELPB_BUTTON,
             disable_web_page_preview=True
         )  
         await update.answer(
             text="🔱 𝕷𝖔𝖌𝖔 🔱",
         )         
    elif update.data == "songg":
         await update.message.edit_text(
             text=SONG_STRING,
             reply_markup=HELPB_BUTTON,
             disable_web_page_preview=True
         )
         await update.answer(
             text="🔱 🇸 🇴 🇳 🇬 🇸 🔱", 
         )
    elif update.data == "qrg":
         await update.message.edit_text(
             text=QR_STRING,
             reply_markup=HELPB_BUTTON,
             disable_web_page_preview=True
         )
         await update.answer(
             text="🔱 𝗤𝗥 𝗚𝗘𝗡𝗘𝗥𝗔𝗧𝗢𝗥 🔱",
         )
    elif update.data == "htgm":
         await update.message.edit_text(
             text=TELEGRAPH,
             reply_markup=HHHELP_BUTTONS,
             disable_web_page_preview=True
         )
         await update.answer(
             text="🔱 𝕿𝖊𝖑𝖊𝖌𝖗𝖆𝖕𝖍 🔱",
         )
    elif update.data == "hlogoc":
         await update.message.edit_text(
             text=LOGO_STRING,
             reply_markup=HHHELP_BUTTONS,
             disable_web_page_preview=True
         )  
         await update.answer(
             text="🔱 𝕷𝖔𝖌𝖔 🔱",
         )         
    elif update.data == "hsongg":
         await update.message.edit_text(
             text=SONG_STRING,
             reply_markup=HHHELP_BUTTONS,
             disable_web_page_preview=True
         )
         await update.answer(
             text="🔱 🇸 🇴 🇳 🇬 🇸 🔱",
         )
    elif update.data == "hqrg":
         await update.message.edit_text(
             text=QR_STRING,
             reply_markup=HHHELP_BUTTONS,
             disable_web_page_preview=True
         )
         await update.answer(
             text="🔱 𝗤𝗥 𝗚𝗘𝗡𝗘𝗥𝗔𝗧𝗢𝗥 🔱",
         )    
    elif update.data == "cmds":
         await update.message.edit_text(
             text=HELP_STRING,
             reply_markup=HELP_BUTTONS,
             disable_web_page_preview=True
         ) 
         await update.answer(
             text="🌴 𝗛𝗲𝗹𝗽 🌴",  
         ) 
    elif update.data == "helpb":
         await update.message.edit_text(
             text=HELP_STRING,
             reply_markup=HELP_BUTTONS,
             disable_web_page_preview=True
         )
         await update.answer(
             text="🍃 𝗕𝗔𝗖𝗞 🍃",  
         )
    elif update.data == "hhbak":
         await update.message.edit_text(
             text=HELP_STRING,
             reply_markup=GHELP_BUTTONS,
             disable_web_page_preview=True
         )
         await update.answer(
             text="🍃 𝗕𝗔𝗖𝗞 🍃",  
         )
    elif update.data == "ppbak":
         await update.message.edit_text(
             text=HELP_STRING,
             reply_markup=PICMEH_BUTTONS,
             disable_web_page_preview=True
         )
         await update.answer(
             text="🍃 𝗕𝗔𝗖𝗞 🍃",  
         )
    elif update.data == "pbamk":
         await update.message.edit_text(
             text=HELP_STRING,
             reply_markup=PICMEH_BUTTONS,
             disable_web_page_preview=True
         )
         await update.answer(
             text="🍃 𝗕𝗔𝗖𝗞 🍃",  
         )
    elif update.data == "helpp":
         await update.message.edit_text(
             text=HELP_STRING,
             reply_markup=PICMEH_BUTTONS,
             disable_web_page_preview=True
         )
         await update.answer(
             text="🍃 𝗕𝗔𝗖𝗞 🍃",  
         )
    elif update.data == "ptgm":
         await update.message.edit_text(
             text=TELEGRAPH,
             reply_markup=PICMEB_BUTTONS,
             disable_web_page_preview=True
         )
         await update.answer(
             text="🔱 𝕿𝖊𝖑𝖊𝖌𝖗𝖆𝖕𝖍 🔱",
         )
    elif update.data == "plogoc":
         await update.message.edit_text(
             text=LOGO_STRING,
             reply_markup=PICMEB_BUTTONS,
             disable_web_page_preview=True
         )  
         await update.answer(
             text="🔱 𝕷𝖔𝖌𝖔 🔱",
         )         
    elif update.data == "psongg":
         await update.message.edit_text(
             text=SONG_STRING,
             reply_markup=PICMEB_BUTTONS,
             disable_web_page_preview=True
         )
         await update.answer(
             text="🔱 🇸 🇴 🇳 🇬 🇸 🔱",
         )
    elif update.data == "pqrg":
         await update.message.edit_text(
             text=QR_STRING,
             reply_markup=PICMEB_BUTTONS,
             disable_web_page_preview=True
         )
         await update.answer(
             text="🔱 𝗤𝗥 𝗚𝗘𝗡𝗘𝗥𝗔𝗧𝗢𝗥 🔱",
         )     
    elif update.data == "hcmds":
         await update.message.edit_text(
             text=HELP_STRING,
             reply_markup=GHELP_BUTTONS,
             disable_web_page_preview=True
         )
         await update.answer(
             text="🌴 𝗛𝗲𝗹𝗽 🌴",  
         )
    elif update.data == "hbamk":
         text = f"Hi {update.from_user.mention}\n\n**» press the button below to read the explanation and see the list of available commands !**\n\n__⚡️ Powered by ⚡️__[𝕯𝖆𝖗𝖐 𝕰𝖒𝖕𝖎𝖗𝖊 🇱🇰🇸 🇱 🇧 🇴 🇹 🇸 ™](t.me/SL_BOTS_TM)"
         reply_markup = InlineKeyboardMarkup([[
                 InlineKeyboardButton(text="𝗛𝗲𝗹𝗽⁉️",callback_data="hcmds")
                 ]]
                 )
         await update.message.edit_text(
             text=text,
             reply_markup=reply_markup,
             disable_web_page_preview=True
         ) 
         await update.answer(
             text="🍃 𝗕𝗔𝗖𝗞 🍃",  
         )
    elif update.data == "ref":
         await update.answer(
             text="♻️Reloading.....♻️",
         )
    elif update.data == "picme":
        await update.answer("....🔱 𝗣𝗶𝗰 𝗺𝗲 🔱....\nCapture started...Creating Your dp")
        PICME_TEXT = f"""
**Now You can Create your Image Useing Me!**
 Pic me : Capture Your Profile Picture.

Send To Inbox Automatically You must start
[This Bot](https://t.me/darks_pm_bot)

User : {update.from_user.mention}
"""
        photoid = update.from_user.photo.big_file_id  
        photo = await bot.download_media(photoid)
        await update.edit_message_media(InputMediaPhoto(media=photo, caption=PICME_TEXT), reply_markup=picmebtns)
        await Client.send_photo(update.from_user.id, photo=photo, caption=PICME_TEXT.format(update.from_user.mention))
        os.remove(photo)
    elif update.data == "add":
         await update.answer(
             text="Adding Soon....",
         )    
		
@Client.on_callback_query()
async def cb_data(bot, update):
        data = update.data
        try:
            message_text = update.message.text.split("\n")[0].strip().split("=")[0].strip()
            message_text = '' if CALCULATE_TEXT in message_text else message_text
            if data == "=":
                text = float(eval(message_text))
            elif data == "DEL":
                text = message_text[:-1]
            elif data == "AC":
                text = ""
            else:
                text = message_text + data
            await update.message.edit_text(
                text=f"{text}\n\n{CALCULATE_TEXT}",
                disable_web_page_preview=True,
                reply_markup=CALCULATE_BUTTONS
            )
        except Exception as error:
            print(error)
	

@Client.on_inline_query()
async def inline(bot, update):
    if len(update.data) == 0:
        try:
            answers = [
                InlineQueryResultArticle(
                    title="Calculator",
                    description=f"New calculator",
                    input_message_content=InputTextMessageContent(
                        text=CALCULATE_TEXT,
                        disable_web_page_preview=True
                    ),
                    reply_markup=CALCULATE_BUTTONS
                )
            ]
        except Exception as error:
            print(error)
    else:
        try:
            message_text = update.message.text.split("\n")[0].strip().split("=")[0].strip()
            data = message_text.replace("×", "*").replace("÷", "/")
            text = float(eval(data))
            answers = [
                InlineQueryResultArticle(
                    title="Answer",
                    description=f"Results of your input",
                    input_message_content=InputTextMessageContent(
                        text=f"{data} = {text}",
                        disable_web_page_preview=True
                    )
                )
            ]
        except:
            pass
    await update.answer(answers)	
		


		
