import detect
import rfid
import camera
import time
from progress.counter import Countdown
import connect

card_id = None
seat_id = 12

while True:

    temp_id = rfid.read_id()
    if temp_id != None:
        card_id = temp_id
    if card_id != None:
        print("当前卡号：", card_id)
    else:
        print("未刷卡！！")

    camera.capture()

    have_person, have_obj = detect.detect()

    print("上传刷卡信息")
    if card_id!=None:
        connect.put_state(seat_id, 0, None, 1)
    else:
        connect.put_state(seat_id, 1, card_id, 1)
    
    print("上传座位状态")
    if have_obj and have_person:
        connect.put_state(seat_id, 4, card_id, 2)
    elif have_person:
        connect.put_state(seat_id, 2, card_id, 2)
    elif have_obj:
        connect.put_state(seat_id, 3, card_id, 2)
    else:
        connect.put_state(seat_id, 1, card_id, 2)


    countdown = Countdown("距离下一次检测倒计时（秒）", max=30)
    for i in range(30):
        time.sleep(1)
        countdown.next()
    print("\n**************************************************\n")
