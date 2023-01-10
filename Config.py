import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "29653892"))
    API_HASH = os.environ.get("API_HASH", "9a9c203c27ccb3a6d3982ecdab9c54ad")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5923479429:AAGg-tMOrWMOKWxdFgDCGPPjm5tBgIVgD88")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1AZWarzoBu3GBvXSXoTkS7u4Qz5adZZOObalhdf2Aeeyh0tg3-dFb-BJ7LhV4fBPmz3T5MdS9naovIHQJN2dYsJBb5qqqw7Wq0dQMWMd8z40pm-XFGaPJ05zJpeTBQYs3Fm6FQfcu9eQu-d1I4pVb9XCS8PJk7Bzh6AQfgvSVMFrxCJxzb7Dg6xmh1M-D1ZNqWRSWzv2-zcBVR_06PmpPEEfu0j0qTy6PljgV1THv_sf4ZuJA1e8F4PV4_KWJNU5_ijBGE73k1Wi21rjxwJITUF2v8A-ROlcDoRIDDxDXQwQ7Pm210CfEOb-fhX_FDq7tQYxvnQRClTk35SqWzZXVi5yjeC3C-c0=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "F4R_MUSIC_BOT")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5663329994")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"
