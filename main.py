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

   ___  ___   ___  __ ______  ___  __  ___  ___  ____  ______
  / _ \/ _ | / _ \/ //_/ __/ / _ \/  |/  / / _ )/ __ \/_  __/
 / // / __ |/ , _/ ,< _\ \  / ___/ /|_/ / / _  / /_/ / / /   
/____/_/ |_/_/|_/_/|_/___/ /_/  /_/  /_/ /____/\____/ /_/   
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
➖➖➖➖➖➖➖➖➖➖
@{uname} Started Successfully!
➖➖➖➖➖➖➖➖➖➖
join: @SLBotOfficial
➖➖➖➖➖➖➖➖➖➖
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
""")

idle()
