from pyrogram import filters ,Client
from pyrogram.errors import PeerIdInvalid
import os

@Client.on_message(filters.private & filters.command('info'))
async def pinfo(bot, update):
    x=await update.reply_text('`getting a user....`')
    if update.reply_to_message:
        try:
            photoid =update.reply_to_message.from_user.photo.big_file_id
            photo = await bot.download_media(photoid)
            await bot.delete_messages(update.chat.id ,x.id)
            await update.reply_photo(photo ,
            caption=f"""User Info :
ID : `{update.reply_to_message.from_user.id}`
First Name : `{update.reply_to_message.from_user.first_name}`
Last_name : `{update.reply_to_message.from_user.last_name}`
Permenet Link : {update.reply_to_message.from_user.mention}
Verified : `{update.reply_to_message.from_user.is_verified}`
Is A Bot : `{update.reply_to_message.from_user.is_bot}`
Is Premium : `{update.reply_to_message.from_user.is_premium}`
""")        
            os.remove(photo)
        except:
            await bot.delete_messages(update.chat.id ,x.id)
            await update.reply_text(f"""User info:
ID : `{update.reply_to_message.from_user.id}`
First Name : `{update.reply_to_message.from_user.first_name}`
Last_name : `{update.reply_to_message.from_user.last_name}`
Permenet Link : {update.reply_to_message.from_user.mention}
Verified : `{update.reply_to_message.from_user.is_verified}`
Is A Bot : `{update.reply_to_message.from_user.is_bot}`
Is Premium : `{update.reply_to_message.from_user.is_premium}`
""")

    elif len(update.command) == 1:
        try:
            photoid =update.from_user.photo.big_file_id
            photo = await bot.download_media(photoid)
            await bot.delete_messages(update.chat.id ,x.id)
            await update.reply_photo(photo ,caption=f"""User Info :
ID : `{update.from_user.id}`
First Name : `{update.from_user.first_name}`
Last_name : `{update.from_user.last_name}`
Permenet Link : {update.from_user.mention}
Verified : `{update.from_user.is_verified}`
Is A Bot : `{update.from_user.is_bot}`
Is Premium : `{update.from_user.is_premium}`
""")
        except:
            await bot.delete_messages(update.chat.id ,x.id)
            await update.reply_text(f"""User Info :
ID : `{update.from_user.id}`
First Name : `{update.from_user.first_name}`
Last_name : `{update.from_user.last_name}`
Permenet Link : {update.from_user.mention}
Verified : `{update.from_user.is_verified}`
Is A Bot : `{update.from_user.is_bot}`
Is Premium : `{update.from_user.is_premium}`
""")    
            
    else:
        u = update.command[1]
        try:
            user=await bot.get_users(u)
            try:
                photoid =user.photo.big_file_id
                photo = await bot.download_media(photoid)
                await bot.delete_messages(update.chat.id ,x.id)
                await update.reply_photo(photo ,caption=f"""User Info:
ID : `{user.id}`
First Name : `{user.first_name}`
Last_name : `{user.last_name}`
Permenet Link : {user.mention}
Verified : `{user.is_verified}`
Is A Bot : `{user.is_bot}`
Is Premium : `{user.is_premium}`
            """)
                os.remove(photo)
            except:
                await bot.delete_messages(update.chat.id ,x.id)
                await update.reply_text(f"""User Info :
ID : `{user.id}`
First Name : `{user.first_name}`
Last_name : `{user.last_name}`
Permenet Link : {user.mention}
Verified : `{user.is_verified}`
Is A Bot : `{user.is_bot}`
Is Premium : `{user.is_premium}`
                """)
        except :
            await bot.delete_messages(update.chat.id ,x.id)
            await update.reply_text("`User not Found!`")       
     
        
@Client.on_message(filters.group & filters.command('info'))
async def ginfo(bot, update):
    a=await update.reply_text('`getting an info.....`')
    if update.reply_to_message:
        st=await bot.get_chat_member(update.chat.id , update.reply_to_message.from_user.id)
        try:
            photoid =update.reply_to_message.from_user.photo.big_file_id
            photo = await bot.download_media(photoid)
            await bot.delete_messages(update.chat.id ,a.id)
            await update.reply_photo(photo,caption=f"""User Info:
ID : `{update.reply_to_message.from_user.id}`
First Name : `{update.reply_to_message.from_user.first_name}`
Last_name : `{update.reply_to_message.from_user.last_name}`
Permenet Link : {update.reply_to_message.from_user.mention}
Verified : `{update.reply_to_message.from_user.is_verified}`
Is A Bot : `{update.reply_to_message.from_user.is_bot}`
Is Premium : `{update.reply_to_message.from_user.is_premium}`
joined_date : `{st.joined_date}`
Status : `{st.status}`            
""")
        except:
            await bot.delete_messages(update.chat.id ,a.id)
            await update.reply_text(f"""User Info :
ID : `{update.reply_to_message.from_user.id}`
First Name : `{update.reply_to_message.from_user.first_name}`
Last_name : `{update.reply_to_message.from_user.last_name}`
Permenet Link : {update.reply_to_message.from_user.mention}
Verified : `{update.reply_to_message.from_user.is_verified}`
Is A Bot : `{update.reply_to_message.from_user.is_bot}`
Is Premium : `{update.reply_to_message.from_user.is_premium}`
joined_date : `{st.joined_date}`
Status : `{st.status}`
""")    
        

    elif len(update.command) == 1:
        chat=await bot.get_chat(update.chat.id)
        try:
            photoid =chat.photo.big_file_id
            photo = await bot.download_media(photoid)
            await bot.delete_messages(update.chat.id ,a.id)
            await update.reply_photo(photo ,caption=f"""Chat Info:
ID : `{chat.id}`
Title : `{chat.title}`
Chat Type : `{chat.type}`
description : `{chat.description}`
Member Count : `{chat.members_count}`
""")     
        except:
            await bot.delete_messages(update.chat.id ,a.id)
            await update.reply_text(f"""Chat Info :
ID : `{chat.id}`
Title : `{chat.title}`
Chat Type : `{chat.type}`
description : `{chat.description}`
Member Count : `{chat.members_count}`
""")     

    else:
        u = update.command[1]
        try:
            user=await bot.get_users(u)
            ust=await bot.get_chat_member(update.chat.id ,u)
            try:
                photoid =chat.photo.big_file_id
                photo = await bot.download_media(photoid)
                await bot.delete_messages(update.chat.id ,a.id)
                await update.reply_photo(photo ,caption=f"""User Info :
ID : `{user.id}`
First Name : `{user.first_name}`
Last_name : `{user.last_name}`
Permenet Link : {user.mention}
Verified : `{user.is_verified}`
Is A Bot : `{user.is_bot}`
joined_date : `{ust.joined_date}`
Status : `{ust.status}`
""")
            except:
                await bot.delete_messages(update.chat.id ,a.id)
                await update.reply_text(f"""User Info:
ID : `{user.id}`
First Name : `{user.first_name}`
Last_name : `{user.last_name}`
Permenet Link : {user.mention}
Verified : `{user.is_verified}`
Is A Bot : `{user.is_bot}`
joined_date : `{ust.joined_date}`
Status : `{ust.status}`
            """)
        
        except :
            await bot.delete_messages(update.chat.id ,a.id)
            await update.reply_text("`User not Found!`") 
