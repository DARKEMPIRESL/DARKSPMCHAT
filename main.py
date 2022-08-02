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

 ____    ______  ____    __  __   ____        ____                 ____     _____   ______   
/\  _`\ /\  _  \/\  _`\ /\ \/\ \ /\  _`\     /\  _`\   /'\_/`\    /\  _`\  /\  __`\/\__  _\  
\ \ \/\ \ \ \L\ \ \ \L\ \ \ \/'/'\ \,\L\_\   \ \ \L\ \/\      \   \ \ \L\ \\ \ \/\ \/_/\ \/  
 \ \ \ \ \ \  __ \ \ ,  /\ \ , <  \/_\__ \    \ \ ,__/\ \ \__\ \   \ \  _ <'\ \ \ \ \ \ \ \  
  \ \ \_\ \ \ \/\ \ \ \\ \\ \ \\`\  /\ \L\ \   \ \ \/  \ \ \_/\ \   \ \ \L\ \\ \ \_\ \ \ \ \ 
   \ \____/\ \_\ \_\ \_\ \_\ \_\ \_\\ `\____\   \ \_\   \ \_\\ \_\   \ \____/ \ \_____\ \ \_\
    \/___/  \/_/\/_/\/_/\/ /\/_/\/_/ \/_____/    \/_/    \/_/ \/_/    \/___/   \/_____/  \/_/
                                                                                             
                                                                                             
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
➖➖➖➖➖➖➖➖➖➖
@{uname} Started Successfully!
➖➖➖➖➖➖➖➖➖➖
join: @SLBotOfficial
➖➖➖➖➖➖➖➖➖➖
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
""")

idle()
