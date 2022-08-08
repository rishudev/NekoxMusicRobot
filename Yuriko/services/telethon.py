import os
from telethon import TelegramClient

from Yuriko import TOKEN, API_ID, API_HASH

TOKEN = os.environ.get("TOKEN")
NAME = TOKEN.split(":")[0]

tbot = TelegramClient(
    NAME, API_ID, API_HASH
) 


# Telethon
tbot.start(bot_token=TOKEN)
