from pyrogram import filters ,Client
from pyrogram.errors import ChatAdminRequired ,UserAdminInvalid,MessageEmpty
from pyrogram import enums

@Client.on_message(filters.group & filters.command('pin'))
async def pin(bot, update):
    me=await bot.get_me()
    st= await bot.get_chat_member(update.chat.id, update.from_user.id)
    
    try:
        try:
            if st.privileges.can_restrict_members ==True:
                if update.reply_to_message:
                    message_id=update.reply_to_message_id
                    try:
                        await bot.pin_chat_message(chat_id=update.chat.id,message_id=message_id)
                        if update.chat.username:
                            link_chat_id = update.chat.username
                            message_link = f"https://t.me/{link_chat_id}/{message_id}"
                        elif (str(update.chat.id)).startswith("-100"):
                            link_chat_id = (str(update.chat.id)).replace("-100", "")
                            message_link = f"https://t.me/c/{link_chat_id}/{message_id}"
                        return await update.reply_text(f"succefully pin [message]({message_link})")
                    except UserAdminInvalid:
                            await update.reply_text("I'm not admin")

                elif len(update.command) == 1:
                    await update.reply_text(
                    "hey ,what I pin",
                    quote=True,)
            
                
            else:
                await update.reply_text("you're not an admin")
        except :
           await update.reply_text(f"`oops! something went wrong!`  ")

    except ChatAdminRequired:
        await update.reply_text("I'm not an admin .")

@Client.on_message(filters.group & filters.command('pinned'))
async def pined(bot, update):
    chat_title = update.chat.title
    chat = await bot.get_chat(chat_id=update.chat.id)
    print(chat.pinned_message.id)
    
    if chat.pinned_message:
        pinned_id = chat.pinned_message.id
        if update.chat.username:
            link_chat_id = update.chat.username
            message_link = f"https://t.me/{link_chat_id}/{pinned_id}"
        elif (str(update.chat.id)).startswith("-100"):
            link_chat_id = (str(update.chat.id)).replace("-100", "")
            message_link = f"https://t.me/c/{link_chat_id}/{pinned_id}"

        await update.reply_text(
            f"The last pinned message of {chat_title} is [here]({message_link}).",
            disable_web_page_preview=True,
        )
    
