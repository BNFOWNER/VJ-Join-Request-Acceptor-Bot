from os import environ

API_ID = int(environ.get("API_ID", "17437151"))
API_HASH = environ.get("API_HASH", "989b5edde691789c36764704e050a072")
BOT_TOKEN = environ.get("BOT_TOKEN", "7829335477:AAEQk4EUggNFsnReYmni7_bN64q33Tl4PnM")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002429100121"))
ADMINS = int(environ.get("ADMINS", "6952679913"))
DB_URI = environ.get("DB_URI", "mongodb+srv://bharathkalladi38:4TDnaR1dZqAEshQq@cluster0.ps5ucul.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = environ.get("DB_NAME", "vjjoinrequetbot")
