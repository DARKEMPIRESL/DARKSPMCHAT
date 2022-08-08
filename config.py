import os

#Vars
BOT_TOKEN = os.getenv("BOT_TOKEN", "")  # from @botfather
API_ID = int(os.getenv("API_ID", ""))  # from https://my.telegram.org/apps
API_HASH = os.getenv("API_HASH", "")  # from https://my.telegram.org/apps
MUST_JOIN = os.getenv("MUST_JOIN", "SLBotOfficial")
OWNER_ID = int(os.environ.get("OWNER_ID", "1120271521"))
ARQ_API_URL = os.environ.get("ARQ_API_URL")
ARQ_API_KEY = os.environ.get("ARQ_API_KEY")
DATABASE_URL = os.environ.get('DATABASE_URL', None)
DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")


DEVS = [1120271521]
