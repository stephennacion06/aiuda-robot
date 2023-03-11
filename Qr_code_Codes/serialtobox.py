import serial
import time
ser2 = serial.Serial(port='/dev/ttyUSB0', baudrate=9600,timeout=1)
ser2.flush()
box_1=0
box_2=0
box_3=0
box_4=0
box_5=0
box_6=0
box_7=0
box_8=0
box_9=0
box_10=0
box_11=0
box_12=0
box_list = [box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9,box_10]
box_list = "[{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11}]\n".format(box_1,
            box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9,box_10, box_11, box_12)

while True:
    ser2.write(box_list.encode())

ser2.close()



	
