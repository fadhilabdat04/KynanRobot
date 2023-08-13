class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 12857763
    API_HASH = "7b71e8bca0d5e1c6d8383ae818d9ec8d"

    ARQ_API_KEY = "PBXFMD-NWMWEN-FMFLQP-JBGTTF-ARQ"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://cmumeqmp:s_gXyCS_rRIXftIQKoqKRush_NeRvw4d@rosie.db.elephantsql.com/cmumeqmp"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1001795374467)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://fadhil01:fadhil123@fadhil01.s6lkqsq.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/d2f257710e964cd8aa0db.jpg"
    
    DONATE_LINK = "https://telegra.ph//file/2299c3cfec6ef92db4fad.jpg"

    SUPPORT_CHAT = "SiArabGroup"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "6515197149:AAEicDMoVIsS5KfEPpIorYEsLyuuxX55xkk"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "00QLM6VO01TS"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 1948147616  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = [0]  # List of groups that you want blacklisted.
    DRAGONS = [1948147616]  # User id of sudo users
    DEV_USERS = [1948147616]  # User id of dev users
    DEMONS = [1948147616]  # User id of support users
    TIGERS = [1948147616]  # User id of tiger users
    WOLVES = [1948147616]  # User id of whitelist users

    ALLOW_CHATS = True
    OWNER_USERNAME = "Dhilnihnge"
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
