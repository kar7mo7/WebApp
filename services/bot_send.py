import requests
from datetime import datetime


def send_msg(**kwargs):
    token = "6591189150:AAHslrig32Zk9W9OZEqRw7ZFszEb5-WN4XM"  # bot token

    user_id = "1967647963"  # user id
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + user_id + "&text=" + f"{datetime.now().strftime(f'<b>%d/%m/%y  %H : %M : %S {kwargs}</b>')}&parse_mode=HTML"
    response = requests.get(url_req)
    print(response.json())

