import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from util.bot_toks import main_bot_tok

userId = ""

print("Bot started")

vk_session = vk_api.VkApi(token=main_bot_tok)
vk = vk_session.get_api()
longpull = VkLongPoll(vk_session)




def sendMessage(id, text):
    vk.messages.send(user_id=id, message=text, random_id=0)


for event in longpull.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            msg = event.text.lower()
            id = event.user_id
            if msg == "хай":
                sendMessage(id, "И тебе даров")
            elif msg == "начать":
                sendMessage(id, "Привет, добро пожаловать к боту!")
            else:
                sendMessage(id, "Я тебя не понимаю!")
