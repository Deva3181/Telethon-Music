import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 6079884294:AAE-mXhtYyrhD2Z9ivF791yID77x87pOGLo)
    STRING_SESSION = os.environ.get("STRING_SESSION", 1BVtsOLsBuxy_ETBaW5zkmboSBUBZycfHaAYS9Qwe-TrK94yqYIh2smh1WkFfzwpmTx_sWjPyMLdvSNzKCW-jPutZNVS9yCO2wFCFU8y7wSVJtcWIenvCUnOnvbRUYIxaoDaI4lqF7Au6rsIxCTlVCtduRQFb8AkmtL1ffQrNeIPkpLj4YSsC3d09AwWd-ROroYUz1vxxm-DIKGqndLRPDLcywR67DYSmf1FuLfGqzILfRme3nyTlutDw7K_eWs_H-X5GAcJaKOJmuAyK94qGKvzVzDWr2HRyuC_LfnModCZaq1sWH81rr5ZMMA_NjMW-8aJyxYzYxdzCVCjgwYe0a4FA82-MrwE=)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "6079884294")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
