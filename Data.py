from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}.
Welcome to {}
I am the Master of Whisperers (like Varys in Game of Thrones).
You can use me to send whispers to your friend in groups and channels (even if I'm not there).
Only that friend and you will be able to read the message even though others are in same group. 
To see how to use me press 'How to Use' below.
By @SL_BOTS_TM
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("π Send a Whisper π", switch_inline_query="")],
        [InlineKeyboardButton(text="π  Return Home π ", callback_data="home")],
    ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("π Send a Whisper π", switch_inline_query="")
        ],
        [InlineKeyboardButton("π€ Bot Status and More Bots π€", url="https://t.me/SLBotOfficial/28")],
        [
            InlineKeyboardButton("β How to Use β", callback_data="help"),
            InlineKeyboardButton("βΎοΈ About βΎοΈ", callback_data="about")
        ],
        [InlineKeyboardButton("β₯ More Amazing bots β₯", url="https://t.me/SLBotOfficial")],
        [InlineKeyboardButton("π« Support Group π«", url="https://t.me/SLBotsChat")]
    ]

    # Help Message
    HELP = """
Just type the message in below format in any chat.
`@darks_pm_bot your_message friend_username/id`
    """

    # About Message
    ABOUT = """
**About This Bot** 
Bot created by @SLBotOfficial
Source Code : [Click Here](https://github.com/DARKEMPIRESL/DARKSPMCHAT)
Framework : [Pyrogram](docs.pyrogram.org)
Language : [Python](www.python.org)
Developer : @ImDark_Empire
    """
