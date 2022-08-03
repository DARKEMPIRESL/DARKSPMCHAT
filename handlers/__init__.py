import aiohttp
from pyrogram import Client
from config import *
from telethon import TelegramClient
from pyromod import listen

pbot = Client("DARKSPM-Pyrogram", bot_token=BOT_TOKEN,
             api_hash=API_HASH, api_id=API_ID,)
tbot = TelegramClient("DARKSPM-Telethon", api_id=API_ID, api_hash=API_HASH)
aiohttpsession = aiohttp.ClientSession()
