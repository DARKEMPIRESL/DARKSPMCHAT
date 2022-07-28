from pyrogram import Client
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent
import ast
import json
from pyrogram import Client
from pyrogram.types import (
    InlineQueryResultArticle,
    InputTextMessageContent,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ChosenInlineResult
)
from pyrogram.errors import UsernameInvalid, UsernameNotOccupied, PeerIdInvalid
from handlers.database.whisper_sql import Whispers
from handlers.database.users_sql import Users
from handlers.database import SESSION
from handlers.bot_users import check_for_users


# Inline Mode
@Client.on_inline_query()
async def answer(_, inline_query):
	await inline_query.answer(
		results=[
			InlineQueryResultArticle(
				title=f"Your Telegram ID is {inline_query.from_user.id}",
				input_message_content=InputTextMessageContent(
					f"My Telegram ID is `{inline_query.from_user.id}`"
				),
				description="Tap to send your ID to current chat",
				thumb_url="https://telegra.ph/file/9b9e7c8c136ee79b17551.jpg",
			)
		],
		cache_time=1,
	)


main = [
    InlineQueryResultArticle(
        title="Whisper Bot",
        input_message_content=InputTextMessageContent("Write Target User's @username or id at the end of your message."),
        url="https://t.me/SLBotOfficial",
        description="Write Target User's @username or id at the end of your message.",
        thumb_url="https://telegra.ph/file/28575e94555f0d5a66d69.jpg",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Learn More", url="https://t.me/darks_pm_bot?start=start")],
                [InlineKeyboardButton("🔒 Send a Whisper 🔒", switch_inline_query="")],
                [InlineKeyboardButton("♥ More Amazing bots ♥", url="https://t.me/SLBotOfficial")]
            ]
        ),
    )
]


@Client.on_chosen_inline_result()
async def _chosen(bot: Client, result: ChosenInlineResult):
    if result.query == "":
        return
    sender = result.from_user.id
    specific = result.inline_message_id
    try:
        str_to_list = result.query.split(" ")
        message = " ".join(str_to_list[:-1])
        receiver = str_to_list[-1]
        to_user = await bot.get_users(receiver)
        receiver_id = to_user.id
        to_user = to_user.__str__()
        SESSION.add(Whispers(specific, message))
        q = SESSION.query(Users).get(sender)
        if q:
            q.target_user = to_user
        else:
            SESSION.add(Users(sender, to_user))
        SESSION.commit()
        await check_for_users([sender, receiver_id])
    except (UsernameInvalid, UsernameNotOccupied, PeerIdInvalid, IndexError):
        message = result.query
        SESSION.add(Whispers(specific, message))
        SESSION.commit()


async def previous_target(sender):
    q = SESSION.query(Users).get(sender)
    if q and q.target_user is not None:
        target_user = q.target_user
        target_user = json.loads(target_user)
        receiver = target_user["id"]
        data_list = [sender, receiver]
        first_name = target_user["first_name"]
        try:
            last_name = target_user["last_name"]
            name = first_name + last_name
        except KeyError:
            name = first_name
        text1 = f"A whisper message to {name}"
        text2 = "Only he/she can open it."
        mention = f"[{name}](tg://user?id={receiver})"
        results = [
              InlineQueryResultArticle(
                  title=text1,
                  input_message_content=InputTextMessageContent(
                      f"A whisper message to {mention}" + " " + text2),
                  url="https://t.me/SLBotOfficial",
                  description=text2,
                  thumb_url="https://telegra.ph/file/9b9e7c8c136ee79b17551.jpg",
                  reply_markup=InlineKeyboardMarkup(
                      [
                          [
                              InlineKeyboardButton(
                                  "🔐 Show Message 🔐",
                                  callback_data=str(data_list),
                              )
                          ]
                      ]
                  ),
              ),
              main[0]
        ]
    else:
        results = main
    return results


# Inline System
@Client.on_inline_query()
async def answer(bot: Client, query):
    query_list = query.query.split(" ")
    sender = query.from_user.id
    if query.query == "":
        await query.answer(
            results=main,
            switch_pm_text="🔒 Learn How to send Whispers",
            switch_pm_parameter="start"
        )
    elif len(query_list) == 1:
        sender = query.from_user.id
        results = await previous_target(sender)
        await query.answer(
            results,
            switch_pm_text="🔒 Learn How to send Whispers",
            switch_pm_parameter="start"
        )
    elif len(query_list) >= 2:
        mentioned_user = query_list[-1]
        try:
            mentioned_user = ast.literal_eval(mentioned_user)
        except (ValueError, SyntaxError):
            pass
        if isinstance(mentioned_user, str) and not mentioned_user.startswith("@"):
            sender = query.from_user.id
            results = await previous_target(sender)
            await query.answer(
                results,
                switch_pm_text="🔒 Learn How to send Whispers",
                switch_pm_parameter="start"
            )
            return
        try:
            target_user = await bot.get_users(mentioned_user)
            sender = query.from_user.id
            receiver = target_user.id
            data_list = [sender, receiver]
            if target_user.last_name:
                name = target_user.first_name + target_user.last_name
            else:
                name = target_user.first_name
            text1 = f"A whisper message to {name}"
            text2 = "Only he/she can open it."
            await query.answer(
                results=[
                    InlineQueryResultArticle(
                        title=text1,
                        input_message_content=InputTextMessageContent(f"A whisper message to {target_user.mention}" + " " + text2),
                        url="https://t.me/SLBotOfficial",
                        description=text2,
                        thumb_url="https://telegra.ph/file/28575e94555f0d5a66d69.jpg",
                        reply_markup=InlineKeyboardMarkup(
                            [
                                [
                                    InlineKeyboardButton(
                                        "🔐 Show Message 🔐",
                                        callback_data=str(data_list),
                                    )
                                ]
                            ]
                        ),
                    )
                ],
                switch_pm_text="🔒 Learn How to send Whispers",
                switch_pm_parameter="start"
            )
            await check_for_users(receiver)
        except (UsernameInvalid, UsernameNotOccupied, PeerIdInvalid,  IndexError):
            sender = query.from_user.id
            results = await previous_target(sender)
            await query.answer(
                results,
                switch_pm_text="🔒 Learn How to send Whispers",
                switch_pm_parameter="start"
            )
    await check_for_users(sender)