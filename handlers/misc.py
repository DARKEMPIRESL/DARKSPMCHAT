import asyncio
import requests
from pyrogram import filters, Client
from gpytranslate import Translator
from pyrogram.errors import PeerIdInvalid
from pyrogram.types import Message, User
from datetime import datetime
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from aiohttp import ClientSession
import os
import re
import aiofiles
from telegraph import upload_file
from io import BytesIO
from traceback import format_exc
from config import *
import pytz
from Python_ARQ import ARQ
from inspect import getfullargspec
import time


loop = asyncio.get_event_loop()
aiohttpsession = ClientSession()
arq = ARQ(ARQ_API_URL, ARQ_API_KEY, aiohttpsession)

@Client.on_message(filters.command("tr"))
async def tr(_, message):
    trl = Translator()
    if message.reply_to_message and (message.reply_to_message.text or message.reply_to_message.caption):
        if len(message.text.split()) == 1:
            target_lang = "en"
        else:
            target_lang = message.text.split()[1]
        if message.reply_to_message.text:
            text = message.reply_to_message.text
        else:
            text = message.reply_to_message.caption
    else:
        if len(message.text.split()) <= 2:
            return await message.reply_text("Provide lang code.\n[Available options](https://telegra.ph/Lang-Codes-02-22).\n<b>Usage:</b> <code>/tr en</code>",disable_web_page_preview=True)
        target_lang = message.text.split(None, 2)[1]
        text = message.text.split(None, 2)[2]
    detectlang = await trl.detect(text)
    try:
        data = requests.get(f"https://api.safone.tech/translate?text={text}&target={target_lang}").json()
        tekstr = await trl(text, targetlang=target_lang)
    except ValueError as err:
        return await message.reply_text(f"Error: <code>{str(err)}</code>")
    return await message.reply_text(f"<b>Translated:</b> from {data['origin']} to {data['target']} \n<code>{data['translated']}</code>")

def ReplyCheck(message: Message):
    reply_id = None
    if message.reply_to_message:
        reply_id = message.reply_to_message.message_id
    elif not message.from_user.is_self:
        reply_id = message.message_id
    return reply_id

infotext = (
    "**[{full_name}](tg://user?id={user_id})**\n"
    " - User id : `{user_id}`\n"
    " - First Name: `{first_name}`\n"
    " - Last Name: `{last_name}`\n"
    " - Username: `{username}`\n"
    " - Last Online: `{last_online}`\n"
    " - Bio: {bio}"
)

def LastOnline(user: User):
    if user.is_bot:
        return ""
    elif user.status == "recently":
        return "Recently"
    elif user.status == "within_week":
        return "Within the last week"
    elif user.status == "within_month":
        return "Within the last month"
    elif user.status == "long_time_ago":
        return "A long time ago :("
    elif user.status == "online":
        return "Currently Online"
    elif user.status == "offline":
        return datetime.fromtimestamp(user.status.date).strftime( "%a, %d %b %Y, %H:%M:%S")

def FullName(user: User):
    return user.first_name + " " + user.last_name if user.last_name else user.first_name

@Client.on_message(filters.command(["info"]))
async def whois(client, message):
    cmd = message.command
    if not message.reply_to_message and len(cmd) == 1:
        get_user = message.from_user.id
    elif len(cmd) == 1:
        get_user = message.reply_to_message.from_user.id
    elif len(cmd) > 1:
        get_user = cmd[1]
        try:
            get_user = int(cmd[1])
        except ValueError:
            pass
    try:
        user = await Client.get_users(get_user)
    except PeerIdInvalid:
        return await message.reply("I don't know that User.")
    desc = await app.get_chat(get_user)
    desc = desc.description
    await message.reply_text(infotext.format(full_name=FullName(user),user_id=user.id,user_dc=user.dc_id,first_name=user.first_name,last_name=user.last_name if user.last_name else "",username=user.username if user.username else "",last_online=LastOnline(user),bio=desc if desc else desc,),disable_web_page_preview=True)

session = ClientSession()
pattern = re.compile(r"^text/|json$|yaml$|xml$|toml$|x-sh$|x-shellscript$")
BASE = "https://batbin.me/"

async def post(url: str, *args, **kwargs):
    async with session.post(url, *args, **kwargs) as resp:
        try:
            data = await resp.json()
        except Exception:
            data = await resp.text()
    return data

async def paste(content: str):
    resp = await post(f"{BASE}api/v2/paste", data=content)
    if not resp["success"]:
        return
    return BASE + resp["message"]


@Client.on_message(filters.command("paste") & ~filters.edited)
async def paste_func(_, message: Message):
    if not message.reply_to_message:
        return await message.reply_text("Reply To A Message With `/paste`")
    r = message.reply_to_message
    if not r.text and not r.document:
        return await message.reply_text("Only text and documents are supported")
    m = await message.reply_text("Pasting...")
    if r.text:
        content = str(r.text)
    elif r.document:
        if r.document.file_size > 40000:
            return await m.edit("You can only paste files smaller than 40KB.")
        if not pattern.search(r.document.mime_type):
            return await m.edit("Only text files can be pasted.")
        doc = await message.reply_to_message.download()
        async with aiofiles.open(doc, mode="r") as f:
            content = await f.read()
        os.remove(doc)
    link = await paste(content)
    kb = [[InlineKeyboardButton(text="Paste Link ", url=link)]]
    try:
        if m.from_user.is_bot:
            await message.reply_photo(photo=link,quote=False,caption="Pasted",reply_markup=InlineKeyboardMarkup(kb),)
        else:
            await message.reply_photo(photo=link,quote=False,caption="Pasted",reply_markup=InlineKeyboardMarkup(kb),)
        await m.delete()
    except Exception:
        await m.edit("Here's your paste", reply_markup=InlineKeyboardMarkup(kb))


@Client.on_message(filters.edited & filters.command(["telegraph", "tm", "tgm"]))
async def telegraph(client, message):
    replied = message.reply_to_message
    if not replied:
        return await message.reply("Reply to a supported media file")
    if not (
        (replied.photo and replied.photo.file_size <= 5242880)
        or (replied.animation and replied.animation.file_size <= 5242880)
        or (replied.video and replied.video.file_name.endswith(".mp4") and replied.video.file_size <= 5242880)
        or (replied.document and replied.document.file_name.endswith((".jpg", ".jpeg", ".png", ".gif", ".mp4")) and replied.document.file_size <= 5242880)):
        return await message.reply("Not supported!")
    download_location = await client.download_media(message=message.reply_to_message,file_name="root/downloads/")
    try:
        response = upload_file(download_location)
    except Exception as document:
        await message.reply(message, text=document)
      
    else:
        await message.reply_text("**♻ ∂σωηℓσα∂ιηg◉❍❍❍❍ ♻**")
        await message.edit_text("**♻ ∂σωηℓσα∂ιηg◉◉❍❍❍ ♻**")
        await message.edit_text("**♻ ∂σωηℓσα∂ιηg◉◉◉❍❍ ♻**")
        await message.edit_text("**♻ ∂σωηℓσα∂ιηg◉◉◉◉❍ ♻**")
        await message.edit_text("**♻ ∂σωηℓσα∂ιηg◉◉◉◉◉ ♻**")
        await update.message.edit_text("**♻️ ◤✞ 𝖕𝖗𝖔𝖈𝖊𝖘𝖘𝖎𝖓𝖌 ✞◥ ♻️ -**") 
        await update.message.edit_text("**♻️ ◤✞ 𝖕𝖗𝖔𝖈𝖊𝖘𝖘𝖎𝖓𝖌 ✞◥ ♻️ \**") 
        await update.message.edit_text("**♻️ ◤✞ 𝖕𝖗𝖔𝖈𝖊𝖘𝖘𝖎𝖓𝖌 ✞◥ ♻️ |**")
        await update.message.edit_text("**♻️ ◤✞ 𝖕𝖗𝖔𝖈𝖊𝖘𝖘𝖎𝖓𝖌 ✞◥ ♻️ /**")
        await update.message.edit_text("**♻️ ◤✞ 𝖕𝖗𝖔𝖈𝖊𝖘𝖘𝖎𝖓𝖌 ✞◥ ♻️ -**") 
        await update.message.edit_text("**♻️ ◤✞ 𝖕𝖗𝖔𝖈𝖊𝖘𝖘𝖎𝖓𝖌 ✞◥ ♻️ \**") 
        await update.message.edit_text("**♻️ ◤✞ 𝖕𝖗𝖔𝖈𝖊𝖘𝖘𝖎𝖓𝖌 ✞◥ ♻️ |**")
        await update.message.edit_text("**♻️ ◤✞ 𝖕𝖗𝖔𝖈𝖊𝖘𝖘𝖎𝖓𝖌 ✞◥ ♻️ /**")
        await update.message.edit_text("**♻️ ◤✞ 𝖕𝖗𝖔𝖈𝖊𝖘𝖘𝖎𝖓𝖌 ✞◥ ♻️ -**") 
        await update.message.edit_text("**♻️ ◤✞ 𝖕𝖗𝖔𝖈𝖊𝖘𝖘𝖎𝖓𝖌 ✞◥ ♻️ \**") 
        await update.message.edit_text("**♻️ ◤✞ 𝖕𝖗𝖔𝖈𝖊𝖘𝖘𝖎𝖓𝖌 ✞◥ ♻️ |**")
        await update.message.edit_text("**♻️ ◤✞ 𝖕𝖗𝖔𝖈𝖊𝖘𝖘𝖎𝖓𝖌 ✞◥ ♻️ /**")
        await update.message.edit_text("**♻️ ◤✞ 𝖕𝖗𝖔𝖈𝖊𝖘𝖘𝖎𝖓𝖌 ✞◥ ♻️ -**") 
        await update.message.edit_text("**♻️ ◤✞ 𝖕𝖗𝖔𝖈𝖊𝖘𝖘𝖎𝖓𝖌 ✞◥ ♻️ \**") 
        await update.message.edit_text("**♻️ ◤✞ 𝖕𝖗𝖔𝖈𝖊𝖘𝖘𝖎𝖓𝖌 ✞◥ ♻️ |**")
        await update.message.edit_text("**♻️ ◤✞ 𝖕𝖗𝖔𝖈𝖊𝖘𝖘𝖎𝖓𝖌 ✞◥ ♻️ /**")
        await update.message.edit_text("**♻️ ◤✞ 𝖕𝖗𝖔𝖈𝖊𝖘𝖘𝖎𝖓𝖌 ✞◥ ♻️ -**") 
        await update.message.edit_text("**♻️ ◤✞ 𝖕𝖗𝖔𝖈𝖊𝖘𝖘𝖎𝖓𝖌 ✞◥ ♻️ \**") 
        await update.message.edit_text("**♻️ ◤✞ 𝖕𝖗𝖔𝖈𝖊𝖘𝖘𝖎𝖓𝖌 ✞◥ ♻️ |**")
        await update.message.edit_text("**♻️ ◤✞ 𝖕𝖗𝖔𝖈𝖊𝖘𝖘𝖎𝖓𝖌 ✞◥ ♻️ /**")
        await message.edit_text("▇░░░░░░░░░░░░░░░░░░░░░░░░")
        await message.edit_text("▇▇░░░░░░░░░░░░░░░░░░░░░░")
        await message.edit_text("▇▇▇░░░░░░░░░░░░░░░░░░░░")
        await message.edit_text("▇▇▇▇░░░░░░░░░░░░░░░░░░")
        await message.edit_text("▇▇▇▇▇░░░░░░░░░░░░░░░░")
        await message.edit_text("▇▇▇▇▇▇░░░░░░░░░░░░░░")
        await message.edit_text("▇▇▇▇▇▇▇░░░░░░░░░░░░")
        await message.edit_text("▇▇▇▇▇▇▇▇░░░░░░░░░░")
        await message.edit_text("▇▇▇▇▇▇▇▇▇░░░░░░░░")
        await message.edit_text("▇▇▇▇▇▇▇▇▇▇░░░░░░")
        await message.edit_text("▇▇▇▇▇▇▇▇▇▇▇░░░░")
        await message.edit_text("▇▇▇▇▇▇▇▇▇▇▇▇░░")
        await message.edit_text("▇▇▇▇▇▇▇▇▇▇▇▇▇")  
        await message.edit_text("**♻ 🅄❍❍❍❍❍ ♻**")
        await message.edit_text("**♻ 🅄🄿❍❍❍❍❍ ♻**")
        await message.edit_text("**♻ 🅄🄿🄻❍❍❍❍❍ ♻**")
        await message.edit_text("**♻ 🅄🄿🄻🄾❍❍❍❍❍ ♻**")
        await message.edit_text("**♻ 🅄🄿🄻🄾🄰❍❍❍❍❍ ♻**")
        await message.edit_text("**♻ 🅄🄿🄻🄾🄰🄳❍❍❍❍❍ ♻**")
        await message.edit_text("**♻ 🅄🄿🄻🄾🄰🄳🄸❍❍❍❍❍ ♻**")
        await message.edit_text("**♻ 🅄🄿🄻🄾🄰🄳🄸🄽❍❍❍❍❍ ♻**")
        await message.edit_text("**♻ 🅄🄿🄻🄾🄰🄳🄸🄽🄶❍❍❍❍❍ ♻**")
        await message.edit_text("**♻ 🅄🄿🄻🄾🄰🄳🄸🄽🄶◉❍❍❍❍ ♻**")
        await message.edit_text("**♻ 🅄🄿🄻🄾🄰🄳🄸🄽🄶◉◉❍❍❍ ♻**")
        await message.edit_text("**♻ 🅄🄿🄻🄾🄰🄳🄸🄽🄶◉◉◉❍❍ ♻**")
        await message.edit_text("**♻ 🅄🄿🄻🄾🄰🄳🄸🄽🄶◉◉◉◉❍ ♻**")
        await message.edit_text("**♻ 🅄🄿🄻🄾🄰🄳🄸🄽🄶◉◉◉◉◉ ♻**")   
        button_s = InlineKeyboardMarkup([[InlineKeyboardButton("Goto Link🔗", url=f"https://telegra.ph{response[0]}")]])
        await message.reply(f"**Link »**\n`https://telegra.ph{response[0]}`",disable_web_page_preview=True,reply_markup=button_s)
    finally:
        os.remove(download_location)

async def quotify(messages: list):
    response = await arq.quotly(messages)
    if not response.ok:
        return [False, response.result]
    sticker = response.result
    sticker = BytesIO(sticker)
    sticker.name = "sticker.webp"
    return [True, sticker]

def getArg(message: Message) -> str:
    arg = message.text.strip().split(None, 1)[1].strip()
    return arg

def isArgInt(message: Message) -> list:
    count = getArg(message)
    try:
        count = int(count)
        return [True, count]
    except ValueError:
        return [False, 0]

@Client.on_message(filters.command(["quote", "q"]))
async def quote(client, message: Message):
    await message.delete()
    if not message.reply_to_message:
        return await message.reply_text("Reply to a message to quote it.")
    if not message.reply_to_message.text:
        return await message.reply_text("Replied message has no text, can't quote it.")
    m = await message.reply_text("`Quoting Message..`")
    if len(message.command) < 2:
        messages = [message.reply_to_message]
    elif len(message.command) == 2:
        arg = isArgInt(message)
        if arg[0]:
            if arg[1] < 2 or arg[1] > 10:
                return await m.edit("Argument must be between 2-10.")
            count = arg[1]
            messages = [i for i in await client.get_messages(message.chat.id,range(message.reply_to_message.message_id,message.reply_to_message.message_id + (count + 5)),replies=0)if not i.empty and not i.media]
            messages = messages[:count]
        else:
            if getArg(message) != "r":
                return await m.edit("Incorrect Argument, Pass **'r'** or **'INT'**, **EX:** __/q 2__")
            reply_message = await client.get_messages(message.chat.id,message.reply_to_message.message_id,replies=1,)
            messages = [reply_message]
    else:
        return await m.edit("Incorrect argument, check quotly module in help section.")
    try:
        if not message:
            return await m.edit("Something went wrong.")
        sticker = await quotify(messages)
        if not sticker[0]:
            await message.reply_text(sticker[1])
            return await m.delete()
        sticker = sticker[1]
        await message.reply_sticker(sticker)
        await m.delete()
        sticker.close()
    except Exception as e:
        await m.edit("Something went wrong while quoting messages,"+ " This error usually happens when there's a "+ " message containing something other than text,"+ " or one of the messages in-between are deleted.")
        e = format_exc()
        print(e)



@Client.on_message(filters.command("invitelink") & ~filters.edited & ~filters.bot & ~filters.private)
async def invitelink(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        return await message.reply_text("Add me as admin of yor group first")
    await message.reply_text(f"**Invite link generated successfully** \n {invitelink}")

