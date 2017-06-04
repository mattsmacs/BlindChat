from endChat import endChat
from startChat import startChat
from utilities import *
import json

def handle_quick_reply(sender, payload, activeChatsDB, waitListDB):

    payload = json.loads(payload)

    if payload["keyword"] == "profile_share":
        endChat(sender, activeChatsDB, payload=payload, sharePromptDone=True)

    elif payload["keyword"] == "gender":
        send_interest_menu(sender=sender, gender=payload["gender"])

    elif payload["keyword"] == "interest":
        print("PAY", payload)
        startChat(sender=sender, gender=payload["gender"],interest="male",\
                  activeChatsDB=activeChatsDB, waitingListDB=waitListDB)
