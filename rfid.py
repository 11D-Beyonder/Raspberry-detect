import serial

ser = serial.Serial("/dev/ttyUSB0", 9600)


def read_id():

    if ser.in_waiting:
        stu_id = ser.read(ser.in_waiting).decode("gbk").replace("卡号：", "")
        return stu_id
    else:
        return None
