import datetime
import requests


data = {"username": "admin", "password": "1234"}
url = "https://cuger.top:8083/login"
header = {"content-type": "application/json"}
req = requests.post(url, json=data, headers=header)
token = req.json()["obj"]["token"]
print("获取token: ", token)


def put_state(seat_id, obj_status, card_id, info_type):
    header = {
        "content-type": "application/json",
        "Authorization": "Bearer{}".format(token),
    }
    data = {
        "seatId": seat_id,
        "status": obj_status,
        "stuCardId": card_id,
        "time": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        "type": info_type,
    }
    url = "https://cuger.top:8083/transaction/upload/"
    req = requests.put(url, json=data, headers=header)
    print(req.json())
