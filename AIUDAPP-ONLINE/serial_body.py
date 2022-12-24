import serial
import time
ser2 = serial.Serial(port='/dev/ttyUSB1', baudrate=9600, bytesize=8)


def send_serial_body(speed, angle):
    control_list = "[{0},{1}]\n".format(speed, angle)
    ser2.write(control_list.encode())
    ser2.close()
