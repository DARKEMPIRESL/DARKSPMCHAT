from pyrogram import Client
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from handlers.database.chats_sql import Chats
from handlers.database import SESSION
from pyrogram.errors import UserNotParticipant
import ast
from Data import Data
from handlers.database.whisper_sql import Whispers
from handlers.bot_users import check_for_users

tick = "✅"
cross = "❌"


# Callbacks
@Client.on_callback_query()
async def _callbacks(bot: Client, callback_query: CallbackQuery):
    user = await bot.get_me()
    mention = user["mention"]
    if callback_query.data.lower() == "supported_media_types":
        chat_id = callback_query.from_user.id
        message_id = callback_query.message.message_id
        await bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=Data.SUPPORTED_MEDIA_TYPES,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(Data.supported_media_buttons),
        )
    elif callback_query.data.lower() == "close":
        chat_id = callback_query.from_user.id
        message_ids = [callback_query.message.message_id, callback_query.message.reply_to_message.message_id]
        await bot.delete_messages(chat_id, message_ids)
    elif callback_query.data.lower() == "everyone":
        user_id = callback_query.from_user.id
        chat_id = callback_query.message.chat.id
        message_id = callback_query.message.message_id
        try:
            chat_user = await bot.get_chat_member(chat_id, user_id)
        except UserNotParticipant:
            return
        if chat_user.status in ["creator", "administrator"]:
            q = SESSION.query(Chats).get(chat_id)
            if q.allow_usage == "Everyone":
                await callback_query.answer("Already set to EVERYONE", show_alert=True)
                SESSION.close()
            else:
                q.allow_usage = "Everyone"
                SESSION.commit()
                await bot.edit_message_reply_markup(
                    chat_id=chat_id,
                    message_id=message_id,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton(f"Allow Usage : Everyone {tick}", callback_data="everyone")],
                        [InlineKeyboardButton(f"Allow Usage : Admins Only {cross}", callback_data="admins_only")]
                    ]),
                )
        else:
            await callback_query.answer("Only admins can change settings.", show_alert=True)
    elif callback_query.data.lower() == "admins_only":
        user_id = callback_query.from_user.id
        chat_id = callback_query.message.chat.id
        message_id = callback_query.message.message_id
        try:
            chat_user = await bot.get_chat_member(chat_id, user_id)
        except UserNotParticipant:
            return
        if chat_user.status in ["creator", "administrator"]:
            q = SESSION.query(Chats).get(chat_id)
            if q.allow_usage == "Admins Only":
                await callback_query.answer("Already set to ADMINS ONLY", show_alert=True)
                SESSION.close()
            else:
                q.allow_usage = "Admins Only"
                SESSION.commit()
                await bot.edit_message_reply_markup(
                    chat_id=chat_id,
                    message_id=message_id,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton(f"Allow Usage : Everyone {cross}", callback_data="everyone")],
                        [InlineKeyboardButton(f"Allow Usage : Admins Only {tick}", callback_data="admins_only")]
                    ]),
                )
        else:
            await callback_query.answer("Only admins can change settings.", show_alert=True)

@Client.on_callback_query()
async def _callbacks(bot, callback_query: CallbackQuery):
	user = await bot.get_me()
	mention = user["mention"]
	if callback_query.data.lower() == "home":
		chat_id = callback_query.from_user.id
		message_id = callback_query.message.message_id
		await bot.edit_message_text(
			chat_id=chat_id,
			message_id=message_id,
			text=Data.START.format(callback_query.from_user.mention, mention),
			reply_markup=InlineKeyboardMarkup(Data.buttons),
		)
	elif callback_query.data.lower() == "about":
		chat_id = callback_query.from_user.id
		message_id = callback_query.message.message_id
		await bot.edit_message_text(
			chat_id=chat_id,
			message_id=message_id,
			text=Data.ABOUT,
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(Data.home_buttons),
		)
	elif callback_query.data.lower() == "help":
		chat_id = callback_query.from_user.id
		message_id = callback_query.message.message_id
		await bot.edit_message_text(
			chat_id=chat_id,
			message_id=message_id,
			text="**Here's How to use me**\n" + Data.HELP,
			disable_web_page_preview=True,
			reply_markup=InlineKeyboardMarkup(Data.home_buttons),
		)
	else:
		cb_data = callback_query.data
		data_list = ast.literal_eval(str(cb_data))
		if callback_query.from_user.id in data_list:
			specific = callback_query.inline_message_id
			q = SESSION.query(Whispers).get(specific)
			if q:
				await callback_query.answer(q.message, show_alert=True)
			else:
				await callback_query.answer("Message Not Found", show_alert=True)
			SESSION.commit()
		else:
			await callback_query.answer("Sorry, you cannot see this whisper as it is not meant for you!", show_alert=True)
		await check_for_users(data_list)
	    elif query.startswith("action"):
        success = await admin_check(bot, callback_query.message, user_id, callback_query)
        if not success:
            return
        main = query.split("+")[1].lower()
        chat_id = int(query.split("+")[2])
        only_owner = await get_only_owner(chat_id)
        creator = True if (await bot.get_chat_member(chat_id, callback_query.from_user.id)).status == "creator" else False
        if only_owner and not creator:
            await callback_query.answer("Only owner can change settings in this chat.", show_alert=True)
            return
        if main in ["on", "off"]:
            current_bool = await get_ignore_service(chat_id)
            if main == "on":
                damn = True
            else:
                damn = False
            if current_bool == damn:
                if current_bool:
                    await toggle_ignore_service(chat_id, False)
                    await callback_query.answer("Now the service messages will be checked too!", show_alert=True)
                else:
                    await toggle_ignore_service(chat_id, True)
                    await callback_query.answer("Now the service messages will not be checked!", show_alert=True)
            # else:
            #     pass
        elif main in ["true", "false"]:
            creator = True if (await bot.get_chat_member(chat_id, callback_query.from_user.id)).status == "creator" else False
            if not creator:
                await callback_query.answer("This is a special setting and can only be changed by owner.", show_alert=True)
                return
            current_bool = await get_only_owner(chat_id)
            if main == "true":
                damn = True
            else:
                damn = False
            if current_bool == damn:
                if current_bool:
                    await toggle_only_owner(chat_id, False)
                    await callback_query.answer("Now admins can change fsub chat and settings!", show_alert=True)
                else:
                    await toggle_only_owner(chat_id, True)
                    await callback_query.answer("Now only owner can change fsub chat and settings!", show_alert=True)
        else:
            current_action = await get_action(chat_id)
            if main == current_action:
                await callback_query.answer(f"{main.capitalize()} is already the action type.", show_alert=True)
                return
            else:
                await change_action(chat_id, main)
        buttons = await action_markup(chat_id)
        await callback_query.message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))
    elif query.startswith("joined"):
        try:
            muted_user_id = int(query.split('+')[1])
        except IndexError:
            # Temporarily catch
            return
        chat_id = callback_query.message.chat.id
        bot_id = (await bot.get_me()).id
        force_chat = await get_force_chat(chat_id)
        bot_chat_member = await bot.get_chat_member(chat_id, bot_id)
        bot_chat_member2 = await bot.get_chat_member(force_chat, bot_id)
        chat = await bot.get_chat(force_chat)
        mention = '@'+chat.username if chat.username else 'the chat'
        if bot_chat_member.status != "administrator":
            await callback_query.answer("I've been demoted from this chat. I can't unmute you now. Sorry!", show_alert=True)
            await bot.send_message(chat_id, "I've been demoted here. Of no use then!")
            return
        if bot_chat_member2.status != "administrator":
            await callback_query.answer("I've been demoted from the force subscribe chat.", show_alert=True)
            await bot.send_message(chat_id, "I've been demoted from the force subscribe chat. Of no use then!")
            return
        not_joined = f"Join {mention} first then try!"
        try:
            if user_id == muted_user_id:
                await bot.get_chat_member(force_chat, user_id)
                await bot.unban_chat_member(chat_id, user_id)
                await callback_query.answer("Good Kid. You can start chatting properly in group now.", show_alert=True)
                await callback_query.message.delete()
            else:
                await callback_query.answer('This message is not for you!', show_alert=True)
        except UserNotParticipant:
            await callback_query.answer(not_joined, show_alert=True)		
