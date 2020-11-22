# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open('{}/SaitamaRobot/{}'.format(os.getcwd(), config),
              'r') as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    #Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 2526912  # integer value, dont use ""
    API_HASH = "e13cdbc90345105474a0889a66b94441"
    TOKEN = "1361559412:AAEmf41s2TslTvldbAQRlxubHeIQ2g4UGgs"  #This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 714651075  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "jackcooleewro"
    SUPPORT_CHAT = 'DrSinsSupport'  #Your own group for support, do not add the @
    JOIN_LOGGER = -403886726  #Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = -403886726  #Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    #RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'something://somewhat:user@hosturl:port/databasename'  # needed for any database modules
    LOAD = []
    NO_LOAD = ['rss', 'cleaner', 'connection', 'math']
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = ""  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    #OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list('elevated_users.json', 'sudos')
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list('elevated_users.json', 'devs')
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list('elevated_users.json', 'supports')
    #List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list('elevated_users.json', 'tigers')
    WOLVES = get_user_list('elevated_users.json', 'whitelists')
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  #Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = 8  # Number of subthreads to use. Set as number of threads your processor uses
    BAN_STICKER = ''  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = 'X5V7UUSQP4SHDCG3'  # Get your API key from https://www.alphavantage.co/support/#api-key
    TIME_API_KEY = 'FR4XK5G5ZM40'  # Get your API key from https://timezonedb.com/api
    WALL_API = '8a77e6db11cb1754731885ff8402d7c2'  #For wallpapers, get one from https://wall.alphacoders.com/api.php
    AI_API_KEY = '3f11c2efdd6123f2187a313a5baf89834682ef80b73063a151f73b64ef4ee741d4c89f0df5aa88ad6d355c56d6c2b8991234fd05692eadfc74a539c5eb303247'  #For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
