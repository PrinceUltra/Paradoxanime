#(©)ᴘᴀʀᴀᴅᴏx_ʙᴏᴛᴢ
#Recoded By @ᴘʀɪɴᴄᴇ_ᴜʟᴛʀᴀᴀ



import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7067972319:AAEJDQGtoLwomyZjtlQTrKMBVFzoZtkrE6Y")
#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "26977508"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "396589629e6705c592bc7fe891dc6e37)

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "--1002066660316"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6193451722"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://gojo18301:pdtNQIwGncJ5rLBJ@cluster0.2er21gk.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

#force sub channel id, if you want enable force sub
FORCESUB_CHANNEL = int(os.environ.get("FORCESUB_CHANNEL", "-1002076990610"))
FORCESUB_CHANNEL2 = int(os.environ.get("FORCESUB_CHANNEL2", "-1001613294962"))
FORCESUB_CHANNEL3 = int(os.environ.get("FORCESUB_CHANNEL3", "-1002094281038"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "𝐇𝐨𝐢 𝐛𝐚𝐤𝐚.. {first}\n\n𝐈 𝐀𝐦 𝐚 𝐅𝐢𝐥𝐞-𝐒𝐭𝐨𝐫𝐞 𝐛𝐨𝐭\n𝐘𝐨𝐮 𝐜𝐚𝐧 𝐚𝐜𝐜𝐞𝐬𝐬 𝐟𝐢𝐥𝐞𝐬 𝐭𝐡𝐫𝐨𝐮𝐠𝐡 𝐚 𝐬𝐩𝐞𝐜𝐢𝐟𝐢𝐜 𝐥𝐢𝐧𝐤 𝐠𝐢𝐯𝐞𝐧 𝐛𝐲 𝐨𝐮𝐫 𝐬𝐦𝐚𝐫𝐭 𝐚𝐧𝐝 𝐡𝐚𝐫𝐝 𝐰𝐨𝐫𝐤𝐢𝐧𝐠 𝐚𝐝𝐦𝐢𝐧..!")
try:
    ADMINS=[6827835777]
    for x in (os.environ.get("ADMINS", "5747064963 6827835777").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "𝐛𝐚𝐤𝐚 𝐲𝐨𝐮 𝐡𝐚𝐯𝐞 𝐭𝐨 𝐣𝐨𝐢𝐧 𝐨𝐮𝐫 𝐜𝐡𝐚𝐧𝐧𝐞𝐥𝐬 𝐟𝐢𝐫𝐬𝐭 𝐭𝐨 𝐚𝐜𝐜𝐞𝐬𝐬 𝐟𝐢𝐥𝐞𝐬..\n\n𝐒𝐨 𝐣𝐨𝐢𝐧 𝐭𝐡𝐞 𝐜𝐡𝐚𝐧𝐧𝐞𝐥𝐬 𝐟𝐢𝐫𝐬𝐭 𝐚𝐧𝐝 𝐭𝐫𝐲 𝐚𝐠𝐚𝐢𝐧....!")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "𝐨𝐲𝐞 𝐨𝐲𝐞 𝐛𝐚𝐤𝐚 𝐝𝐨𝐧𝐭 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐦𝐞 𝐝𝐢𝐫𝐞𝐜𝐭𝐥𝐲 𝐈 𝐰𝐨𝐫𝐤 𝐟𝐨𝐫 𝐨𝐧𝐥𝐲 𝐚𝐝𝐦𝐢𝐧𝐬..!"

ADMINS.append(OWNER_ID)
ADMINS.append(6827835777)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
