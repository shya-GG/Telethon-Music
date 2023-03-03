import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "25273596"))
    API_HASH = os.environ.get("API_HASH", "4780aa80420811b68783b7c8fc9ce24e")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 6018741139:AAHCbrfgPp7TU5pIDGsSmwFkF_M7bAz8M3Q)
    STRING_SESSION = os.environ.get("STRING_SESSION", 1BVtsOLwBu6c6JGzCkxupWNJyg44logh15mNF8ATrJGUKDXeEwW8bVYGKjIrizhmQyU-jY_JUwO6LKjVKqTWK9FaOR1msPzEJ3Dz0KshlaM9YUrVPSX29MK0NhgPpsv-phXjZL2PYh50PzFo_DVdyEneNzQWnuUGuGFUeD34Ut2VqOf0twdEMkaex5avZcMEiIAk9fEg-Rgmy6g3gJ_vX_u8oFvJA_ldNiuvSVj6ewKybY65WWz8wcewYIjw7dez2p5fAbiTKscaYs150UUCV5iVSZz4oyt-kychxJeJAz22ZX28zCdfMhBSrDfJl7oUS7eRSRIq4OhyYBnINK55owgETxFNtYsc=)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Tharamusic_bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5867426333")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
