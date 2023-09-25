import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from util.bot_toks import sms_bomber_bot_tok
from util import AllText
from main import BotFunctions

print("Bot started")

vk_session = vk_api.VkApi(token=sms_bomber_bot_tok)
vk = vk_session.get_api()
longPull = VkLongPoll(vk_session)

txt = AllText
funcs = BotFunctions

for event in longPull.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            msg = str(event.text.lower())
            spirit = event.user_id
            if msg == txt.menu_text.lower():
                funcs.sendMessageBtn(spirit, txt.bot_menu_text)
            elif msg == txt.start_text:
                funcs.sendMessage(spirit, txt.welcome_text)
            elif msg == txt.spam_message_text.lower():
                funcs.sendMessage(spirit, txt.send_your_number_text)
                funcs.sendPhoto(spirit, "data/sample.png")
                funcs.setNewMenu(spirit)
                for event2 in longPull.listen():
                    if event.type == VkEventType.MESSAGE_NEW:
                        if event2.to_me:
                            new_msg = str(event2.text.lower())
                            # +79200622537
                            if new_msg.isdigit():
                                cond = "+" + new_msg.replace("+", "").replace("-", "").replace("(", "").replace(")",
                                                                                                                ""). \
                                    replace(
                                    " ", "")
                                num = cond
                                if num[:3] == "+79" and len(num) == 12:
                                    funcs.sendMessage(spirit, txt.successfully_spamed_text)
                                    break
                                else:
                                    funcs.sendMessage(spirit, txt.number_was_incorrect_text)
                            elif new_msg == txt.cancel_text.lower():
                                funcs.sendMessageBtn(spirit, txt.canceled_text)
                                break
                            else:
                                funcs.sendMessage(spirit, txt.number_was_incorrect_text)
            else:
                funcs.sendMessage(spirit, txt.i_dont_understand_you_text)
