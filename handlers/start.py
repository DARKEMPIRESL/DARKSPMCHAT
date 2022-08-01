from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup


# Start Message
@Client.on_message(filters.private & filters.incoming & filters.command("start"))
async def start(bot, msg):
	user = await bot.get_me()
	mention = user["mention"]
	await bot.send_sticker(msg.chat.id, "CAACAgUAAxkBAAIEIWLh9vxLot7QZlvMp1UT_QrX4O92AAJ5BgACNpEBVcaIt8a3oOWLHgQ")
	await bot.send_message(
		msg.chat.id,
		Data.START.format(msg.from_user.mention, mention),
		reply_markup=InlineKeyboardMarkup(Data.buttons),
	)
