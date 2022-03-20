import os
import re
from youtube_dl import YoutubeDL

class Config:
    APP_ID = int(os.environ.get("APP_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    START_MSG = os.environ.get("START_MSG", " <b>Hello there, I'm Baymax\nI'm a Simple Yet Powerful Bot.Made by [Arosha_Kovida](t.me/Aro_Ediz).  Hit the /help  to visit available commands. </b>\n⠀\n⠀\nᴀʀᴏ|ᴇᴅɪᴢ • ᴘᴜʙʟɪᴄ ᴇᴅɪᴛɪᴏɴ")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/f82649a7e3c951a81006a.png")
    OWNER = os.environ.get("OWNER", "ImAroshaKovida") 
    DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/")
    msg = {}
