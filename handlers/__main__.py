from handlers.plugins import cmds, cback
from pyrogram import idle
from handlers import tbot, pbot
from config import *
from os import listdir
from os.path import isfile, join
import importlib

mypath = 'handlers/plugins'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
Files = []
for file in onlyfiles:
	if file.split('.')[-1] == 'py':
		Files.append(file)
	else:
		pass
Imported = []
for file in Files:
    Imported.append(importlib.import_module(
    	'handlers.plugins.{}'.format(file.split('.')[0])))


tbot.start(bot_token=BOT_TOKEN)
print(BOT_STARTED)
idle()
