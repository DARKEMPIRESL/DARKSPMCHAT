import logging

from pyrogram import Client, idle

from config import *

logging.getLogger("pyrogram").setLevel(logging.INFO)

Client = Client(
    "DARK Pm Bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="handlers"),
)

Client.start()
uname = (Client.get_me()).username
print(f"""


                                                                                                                                            
88888888ba,        db        88888888ba  88      a8P  ad88888ba     88888888ba  88b           d88    88888888ba    ,ad8888ba, 888888888888  
88      `"8b      d88b       88      "8b 88    ,88'  d8"     "8b    88      "8b 888b         d888    88      "8b  d8"'    `"8b     88       
88        `8b    d8'`8b      88      ,8P 88  ,88"    Y8,            88      ,8P 88`8b       d8'88    88      ,8P d8'        `8b    88       
88         88   d8'  `8b     88aaaaaa8P' 88,d88'     `Y8aaaaa,      88aaaaaa8P' 88 `8b     d8' 88    88aaaaaa8P' 88          88    88       
88         88  d8YaaaaY8b    88""""88'   8888"88,      `"""""8b,    88""""""'   88  `8b   d8'  88    88""""""8b, 88          88    88       
88         8P d8""""""""8b   88    `8b   88P   Y8b           `8b    88          88   `8b d8'   88    88      `8b Y8,        ,8P    88       
88      .a8P d8'        `8b  88     `8b  88     "88, Y8a     a8P    88          88    `888'    88    88      a8P  Y8a.    .a8P     88       
88888888Y"' d8'          `8b 88      `8b 88       Y8b "Y88888P"     88          88     `8'     88    88888888P"    `"Y8888Y"'      88       
                                                                                                                                            

                                                                                             
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
@{uname} Started Successfully!
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
join: @SLBotOfficial
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
""")

idle()
