from pyrogram import filters ,Client
from pyrogram.errors import ChatAdminRequired ,UserAdminInvalid,MessageEmpty
from pyrogram import enums
import asyncio

@Client.on_message(filters.command(["json"]))
async def pin(bot, update):
   reply = update.reply_to_message
   if reply:
    try:
        await bot.send_chat_action(update.chat.id, enums.ChatAction.TYPING)
        await asyncio.sleep(1)
        await update.reply_text(f'`{reply}`', quote=True)
    except:
        await bot.send_chat_action(update.chat.id, enums.ChatAction.TYPING)
        await asyncio.sleep(1)
        await update.reply_text('[Error 🚧](t.me/khlhklhbot)', quote=True)
        await bot.send_message(update.from_user.id, '**Replyed Message Is Too Long**')
   else:
    await bot.send_message(update.chat.id, '`Plz Reply To A Msg`')
