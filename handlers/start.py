from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup

STICKERS = ["CAACAgUAAxkBAAIEI2Lh9wABwA5eCscl00ee7IQgUeJ8KAACHgUAAqrCAAFVByHxjhsfLyEeBA", "CAACAgUAAxkBAAIEIWLh9vxLot7QZlvMp1UT_QrX4O92AAJ5BgACNpEBVcaIt8a3oOWLHgQ"]

# Start Message
@Client.on_message(filters.private & filters.incoming & filters.command("start"))
async def start(anonbot, msg):
    print("/start")
    user = await anonbot.get_me()
    mention = user["mention"]
    STICKER = random.choice(STICKERS)
    await anonbot.send_message(
        msg.reply_sticker(STICKER),
        msg.chat.id,
        Data.START.format(msg.from_user.mention, mention),
        reply_markup=InlineKeyboardMarkup(Data.buttons),
    )
