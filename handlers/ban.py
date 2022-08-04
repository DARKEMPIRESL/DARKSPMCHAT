from logging import exception
from pyrogram import filters ,Client
from pyrogram.errors import ChatAdminRequired ,UserAdminInvalid
from pyrogram.types import ChatPrivileges

@Client.on_message(filters.group & filters.command('ban'))
async def ban(bot, update):
    me=await bot.get_me()
    BOT_ID=me.id
    st= await bot.get_chat_member(update.chat.id, update.from_user.id)
    
    try:
        try:
            if st.privileges.can_restrict_members ==True:
                if update.reply_to_message:
                    user_id=update.reply_to_message.from_user.id
                    if user_id == BOT_ID:
                        await update.reply_text(
                        "I can't ban myself, i can leave if you want.")
                    else:
                        try:
                            b=await bot.ban_chat_member(update.chat.id , user_id )
                            return await update.reply_text(f"succefully banned {b.left_chat_member.mention}")
                        except UserAdminInvalid:
                            await update.reply_text("I can't ban this user")

                elif len(update.command) == 1:
                    await update.reply_text(
                    f"Can't find a user...!",
                    quote=True,)
            
                else:
                    u = update.command[1]
                    user=await bot.get_users(u)

                    if BOT_ID == user.id:
                        await update.reply_text(
                        "I can't ban myself, i can leave if you want.")
                    else:
                        b=await bot.ban_chat_member(update.chat.id , user.id )
                        return await update.reply_text(f"succefully banned {b.left_chat_member.mention}")
            else:
                await update.reply_text("you're not an admin")
        except :
           await update.reply_text(f"`oops! something went wrong!`  ")

    except ChatAdminRequired:
        await update.reply_text("I'm not an admin .")


@Client.on_message(filters.group & filters.command('unban'))
async def unban(bot, update):
    me=await bot.get_me()
    BOT_ID=me.id
    st= await bot.get_chat_member(update.chat.id, update.from_user.id)
    if st.privileges.can_restrict_members ==True:
        if update.reply_to_message:
            user_id=update.reply_to_message.from_user.id
            if user_id == BOT_ID:
               await update.reply_text(
                "hey, what the hell.")
            else:
                b=await bot.unban_chat_member(update.chat.id , user_id )
                
                return await update.reply_text(f"succefully unbanned {update.reply_to_message.from_user.mention}")


        elif len(update.command) == 1:
            await update.reply_text(
            f"Can't find  a user...!",
            quote=True,)
            
        else:
            user_id = update.command[1]
            if user_id == BOT_ID:
                update.reply_text(
                "hey,what the hell.")
            else:
                b=await bot.unban_chat_member(update.chat.id , user_id )
                return await update.reply_text(f"succefully unbanned {user_id}")
    else:
            await update.reply_text(f"Your are not admin in {update.chat.title}.")    




@Client.on_message(filters.group & filters.command('kick'))
async def kick(bot, update):
    me=await bot.get_me()
    BOT_ID=me.id
    st= await bot.get_chat_member(update.chat.id, update.from_user.id)
    
    try:
        try:
            if st.privileges.can_restrict_members ==True:
                if update.reply_to_message:
                    user_id=update.reply_to_message.from_user.id
                    if user_id == BOT_ID:
                        await update.reply_text(
                        "Why am I kick ")
                    else:
                        try:
                            b=await bot.ban_chat_member(update.chat.id , user_id )
                            await bot.unban_chat_member(update.chat.id ,user_id)
                            return await update.reply_text(f"succefully kick {b.left_chat_member.mention}")
                        except UserAdminInvalid:
                            await update.reply_text("`I can't kick this user`")

                elif len(update.command) == 1:
                    await update.reply_text(
                    f"Can't find a user...!",
                    quote=True,)
            
                else:
                    u = update.command[1]
                    user=await bot.get_users(u)

                    if BOT_ID == user.id:
                        await update.reply_text(
                        "Why am I kick ")
                    else:
                        b=await bot.ban_chat_member(update.chat.id , user.id )
                        await bot.unban_chat_member(update.chat.id ,user.id)
                        await b.delete()
                        return await update.reply_text(f"succefully kick {b.left_chat_member.mention}")
            else:
                await update.reply_text("you're not an admin")
        except UserAdminInvalid:
           await update.reply_text(f"why I ban an admin  ")

    except ChatAdminRequired:
        await update.reply_text("I'm not an admin .")
