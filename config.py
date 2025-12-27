import os
from os import environ

TG_BOT_TOKEN = os.environ.get("BOT_TOKEN", "8358624438:AAGYd461TjYEbQJsfkgKnXVDDvQdRAT9m9Q")
APP_ID = int(os.environ.get("APP_ID", "26422668"))
API_HASH = os.environ.get("API_HASH", "13853df234b2fbe18d9027a5985cc69e")
OWNER_ID = int(os.environ.get("OWNER_ID", "7527314266"))
PORT = os.environ.get("PORT", "8080")
DB_URL = os.environ.get("DB_URI", "mongodb+srv://villainravangaming:mikey_kun_781_@cluster0.fbgs1zz.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DB_NAME", "villainravangaming")
BOT_USERNAME = os.environ.get("BOT_USERNAME", "Filmy_Dub_Bot")
FSUB_PIC = os.environ.get("FSUB_PIC", "https://ibb.co/FL66q5G9")
START_PIC =os.environ.get("START_PIC", "https://ibb.co/FL66q5G9")
START_MSG = os.environ.get("START_MSG", "<b>Bᴀᴋᴀᴀᴀ...!!!{mention}</b> \n<blockquote><b><i>Iᴀᴍ ᴀ ᴀᴅᴠᴀɴᴄᴇ sᴇǫᴜᴇɴᴄᴇ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴅᴠᴀɴᴄᴇ ғᴇᴀᴛᴜʀᴇs. I ᴄᴀɴ sᴇǫᴜᴇɴᴄᴇ ʏᴏᴜʀ ғɪʟᴇs ᴇᴀsɪʟʏ ɪɴ ᴀ sᴇᴄᴏɴᴅ...!!</i></b></blockquote>")
ABOUT_TXT = os.environ.get("ABOUT_MESSAGE", "<i><b><blockquote>◈ ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/RexBots_Official>RexBots</a>\n◈ ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : <a href=https://t.me/RexBots_Official>RexBOTS</a>\n◈ ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href='https://t.me/about_zani/117'>ZANI</a>\n◈ ᴅᴀᴛᴀʙᴀsᴇ: <a href='https://www.mongodb.com/docs/'>ᴍᴏɴɢᴏ ᴅʙ</a>\n» ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href='https://t.me/about_zani/117'>ZANI</a></blockquote></b></i>")
HELP_TXT =  os.environ.get("HELP_MESSAGE", "⁉️ Hᴇʟʟᴏ {mention} \n<blockquote expandable><b><i>➪ Iᴀᴍ ᴀ ᴘᴜʙʟɪᴄ ғɪʟᴇ(s) sᴇǫᴜᴇɴᴄᴇ ʙᴏᴛ I ᴄᴀɴ sᴇǫᴜᴇɴᴄᴇ ᴛʜᴇ ғɪʟᴇs ᴀɴᴅ ᴀʟsᴏ I ᴄᴀɴ sᴇɴᴅ ᴛʜᴀᴛ ғɪʟᴇs ɪɴ ᴅᴜᴍᴘ ᴄʜᴀɴɴᴇʟ. </i></b></blockquote>")
TG_BOT_WORKERS = 10000
FSUB_LINK_EXPIRY = 300
DATABASE_CHANNEL = int(os.environ.get("DATABASE_CHANNEL", "-1003433236081"))
LOG_FILE_NAME = "links-sharingbot.txt"
SEASON_PATTERN = r'[Ss](\d{1,2})'
EPISODE_PATTERN = r'[Ee][Pp]?(\d{1,3})'
QUALITY_PATTERN = r'(480p|720p|1080p|HDRip|2k|4k)'

TEMP_DIR = "temp_files"
if not os.path.exists(TEMP_DIR):
    os.makedirs(TEMP_DIR)

SORTING_MODES = {
  'Quality': lambda x: (x['quality_order']),
  'All': lambda x: (x['season'], x['episode'], x['quality_order']),
  'Episode': lambda x: (x['episode']),
  'Season': lambda x: (x['season'])
}
QUALITY_ORDER = {
  '480p': 1,
  '720p': 2,
  '1080p': 3,
  'HDRip': 4,
  '2k': 5,
  '4k': 6,
  'unknown': 7
}
