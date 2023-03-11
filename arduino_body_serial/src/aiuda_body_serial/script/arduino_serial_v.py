import serial
import time
import threading
import os

os.system('sudo chmod 777 /dev/ttyUSB0')

# Speed and Angle parameters
angle_path = '/home/aiudabot/AIUDA_PACKAGES/arduino_body_serial/src/aiuda_body_serial/script/angle.txt'
speed_path = '/home/aiudabot/AIUDA_PACKAGES/arduino_body_serial/src/aiuda_body_serial/script/speed.txt'
prev_angle = 0.0
prev_speed = 0.0



body_port = serial.Serial(port='/dev/ttyUSB0', baudrate=115200)

aiuda_body_str = ""


# while True:

#     # Read the Angle and Speed
#     angle_file = open(angle_path, 'r')
#     speed_file = open(speed_path, 'r')

#     #If  angle value is empty use the prev_value
#     try:
#         angle_value = float(angle_file.read())
#         prev_angle = angle_value
#     except:
#         angle_value = prev_angle

#     #If  speed value is empty use the prev_value
#     try:
#         speed_value = float(speed_file.read())
#         prev_speed = speed_value
#     except:
#         speed_value = prev_speed

#     aiuda_body_str = "[" + str(speed_value) + ',' + str(angle_value) + ']\n'

#     if "[" in aiuda_body_str:
#         print(aiuda_body_str)
    # body_port.write(aiuda_body_str.encode())
while True:
    #     # Read the Angle and Speed
    angle_file = open(angle_path, 'r')
    speed_file = open(speed_path, 'r')

    #If  angle value is empty use the prev_value
    try:
        angle_value = float(angle_file.read())
        prev_angle = angle_value
    except:
        angle_value = prev_angle

    #If  speed value is empty use the prev_value
    try:
        speed_value = float(speed_file.read())
        prev_speed = speed_value
    except:
        speed_value = prev_speed
    body_str = [0,0]
    body_str[0] =  speed_value
    body_str[1] =  angle_value
    body_str = str(body_str)+"\n"
    body_port.write(body_str.encode())
    data = body_port.readline()
    if data:
        print(data)