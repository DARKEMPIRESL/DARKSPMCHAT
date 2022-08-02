
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from handlers.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from handlers import Client as app
from handlers import LOGGER



app.start()
LOGGER.info("""
      :::::::::      :::     :::::::::  :::    ::: ::::::::       :::::::::    :::   :::       :::::::::   :::::::: ::::::::::: 
     :+:    :+:   :+: :+:   :+:    :+: :+:   :+: :+:    :+:      :+:    :+:  :+:+: :+:+:      :+:    :+: :+:    :+:    :+:      
    +:+    +:+  +:+   +:+  +:+    +:+ +:+  +:+  +:+             +:+    +:+ +:+ +:+:+ +:+     +:+    +:+ +:+    +:+    +:+       
   +#+    +:+ +#++:++#++: +#++:++#:  +#++:++   +#++:++#++      +#++:++#+  +#+  +:+  +#+     +#++:++#+  +#+    +:+    +#+        
  +#+    +#+ +#+     +#+ +#+    +#+ +#+  +#+         +#+      +#+        +#+       +#+     +#+    +#+ +#+    +#+    +#+         
 #+#    #+# #+#     #+# #+#    #+# #+#   #+# #+#    #+#      #+#        #+#       #+#     #+#    #+# #+#    #+#    #+#          
#########  ###     ### ###    ### ###    ### ########       ###        ###       ###     #########   ########     ###           DARKSPM is online.""")

idle()
