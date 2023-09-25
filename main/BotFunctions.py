import vk_api
from vk_api.longpoll import VkLongPoll
from util.bot_toks import sms_bomber_bot_tok
import json
from util import AllText

txt = AllText

vk_session = vk_api.VkApi(token=sms_bomber_bot_tok)
vk = vk_session.get_api()
longPull = VkLongPoll(vk_session)


def sendMessage(userId, text):
    vk.messages.send(user_id=userId, message=text, random_id=0)


def sendMessageBtn(userId, text):
    vk.messages.send(user_id=userId, message=text, random_id=0, keyboard=keyboard)


def setNewMenu(userId):
    vk.messages.send(user_id=userId, message=txt.your_number, random_id=0, keyboard=keyboard_two)


def sendPhoto(spirit, img):
    upload = vk_api.VkUpload(vk)
    photo = upload.photo_messages(img)
    owner_id = photo[0]['owner_id']
    photo_id = photo[0]['spirit']
    access_key = photo[0]['access_key']
    attachment = f'photo{owner_id}_{photo_id}_{access_key}'
    vk.messages.send(user_id=spirit, attachment=attachment, random_id=0)


def get_but(text, color):
    return {
        "action": {
            "type": "text",
            "payload": "{\"button\": \"" + "1" + "\"}",
            "label": f"{text}"
        },
        "color": f"{color}"
    }


keyboard = {
    "one_time": False,
    "buttons": [
        [get_but(txt.profile_text, "positive")],
        [get_but(txt.spam_message_text, "primary"), get_but(txt.buy_prime_text, "negative")]
    ]
}
keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))

# Another Keyboard
keyboard_two = {
    "one_time": False,
    "buttons": [
        [get_but(txt.cancel_text, "negative")]
    ]
}
keyboard_two = json.dumps(keyboard_two, ensure_ascii=False).encode('utf-8')
keyboard_two = str(keyboard_two.decode('utf-8'))
