import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5731389253:AAFmU--7Ld-HPusJ-NPc5RaUXJr3maANb5c")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOJ8Bu7EMlqhbQndpyVqgl0E7mu8c87M4ZPxT3Kh-5mO5GvYD0qkXD9ysWyfuIMmNXi3oX4sk5SbTkCr5Y82C9XQSNnDHia2AjeGPbTd_KZpLf5g_-INBxPU7bb_d80bSfCpwQYDw9pje68761j-8U-S6oa4s-4jc0duPUuWSXHcBdf1kjV0IKZIvvPHo9Uh0usP6qXK3hYHOfL3Pfp-z8sAzcYX_FuifEaE15nhQdolHqn0-07T0FYrL8a-frI2tJ3oUvMhrUMEsRbYFqpT3V78fxxR_pOHEXq9mwQwsBu9_E5V6KFS3mvQ0hHms8s50jB7xBPO9XvzaJsh9di-9dnBO3iA=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
