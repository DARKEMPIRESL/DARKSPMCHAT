import os
from pyrogram import Client, filters
from pyrogram.types import *
from config import *
from handlers.callbacks import *



START_TEXT = """
Hello {}, I am Telegram [Calculator-Bot](https://Github.com/DARKEMPIRESL/Calculator-Bot).
▷ Send me /calculator and See my Magic.
Made with by ❤️ [𝕯𝖆𝖗𝖐 𝕰𝖒𝖕𝖎𝖗𝖊](https://t.me/ImDark_Empire)
"""
START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🔥 Source Code', url='https://github.com/DARKEMPIRESL/Calculator-Bot'),
        InlineKeyboardButton('Channel 📢', url='https://t.me/SLBotOfficial')
        ]]
    )
CALCULATE_TEXT = "▷ Made with by @SLBotOfficial"
CALCULATE_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton("DEL", callback_data="DEL"),
        InlineKeyboardButton("AC", callback_data="AC"),
        InlineKeyboardButton("(", callback_data="("),
        InlineKeyboardButton(")", callback_data=")")
        ],[
        InlineKeyboardButton("7", callback_data="7"),
        InlineKeyboardButton("8", callback_data="8"),
        InlineKeyboardButton("9", callback_data="9"),
        InlineKeyboardButton("÷", callback_data="/")
        ],[
        InlineKeyboardButton("4", callback_data="4"),
        InlineKeyboardButton("5", callback_data="5"),
        InlineKeyboardButton("6", callback_data="6"),
        InlineKeyboardButton("×", callback_data="*")
        ],[
        InlineKeyboardButton("1", callback_data="1"),
        InlineKeyboardButton("2", callback_data="2"),
        InlineKeyboardButton("3", callback_data="3"),
        InlineKeyboardButton("-", callback_data="-"),
        ],[
        InlineKeyboardButton(".", callback_data="."),
        InlineKeyboardButton("0", callback_data="0"),
        InlineKeyboardButton("=", callback_data="="),
        InlineKeyboardButton("+", callback_data="+"),
        ]]
    )



@Client.on_message(filters.command(["calc", "calculate", "calculator"]))
async def calculate(bot, update):
    await update.reply_text(
        text=CALCULATE_TEXT,
        reply_markup=CALCULATE_BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )


