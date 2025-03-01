if not __name__.endswith("sample_config"):
    import sys
    print(
        "The README is there to be read. Extend this sample config to a config file, don't just rename and change "
        "values here. Doing that WILL backfire on you.\nBot quitting.",
        file=sys.stderr)
    quit(1)


# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "1060722149:AAGEWokvznyR4dHrau1LFVTHs2iN4x_thgg"
    OWNER_ID = "820596651"  # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "am_dq_fan HERE"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'postgresql://anshif_hh0g_user:Rl1xExrjIuoDZ6zlfJt3ABPVmkwbIUBu@dpg-cus0qh56l47c73aet8q0-a.oregon-postgres.render.com/anshif_hh0g'  # needed for any database modules
    MESSAGE_DUMP = None  # needed to make sure 'save from' messages persist
    LOAD = []
    # sed has been disabled after the discovery that certain long-running sed commands maxed out cpu usage
    # and killed the bot. Be careful re-enabling it!
    NO_LOAD = ['translation', 'rss', 'weather', 'sed']
    WEBHOOK = False
    URL = None

    # OPTIONAL
    SUDO_USERS = [1721373213,912095781,1105084940,1205330781,862852632,999873027,644412009,865643300,1769085034,1833664399,1276998600,1555340229,1647428346,1476128450,1734396873,2019529859,1926765024,5574601095,6248131995,5260523032]  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = [
    ]  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = [
    ]  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = True
    STRICT_GMUTE = True
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = 'CAADAgADOwADPPEcAXkko5EB3YGYAg'  # ban sticker
    START_STICKER = True  #add a START_STICKER_ID = 'stickerid' in your config.py if you use this as true
    START_STICKER_ID = 'CAADAgAD0QMAAjq5FQKizo2AiTQCBQI'  #putin hand sticker
    ALLOW_EXCL = False  # Allow ! commands as well as /
    API_OPENWEATHER = None  # OpenWeather API


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
