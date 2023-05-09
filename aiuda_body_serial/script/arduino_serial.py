import serial
import time
import threading
import os

from serial.tools import list_ports

device_list = list_ports.comports()

# Aiuda Body MCU Vendor ID and Product ID
aiudaBodyVid = 6790
aiudaBodyPid = 29987
port = None

for device in device_list:
    if(device.vid != None or device.pid != None):
        print("Initialize Aiuda Cabinet connection")
        if ( device.vid == aiudaBodyVid ) and ( device.pid == aiudaBodyPid ):
            port = device.device
            print("Serial Port Selected: ", port)
            osCmd = "sudo chmod 666 " + port
            os.system(osCmd)
            print("Sucessful setting " + osCmd)
            break

# Speed and Angle parameters
angle_path = '/home/aiudabot/AIUDA_PACKAGES/arduino_body_serial/src/aiuda_body_serial/script/angle.txt'
speed_path = '/home/aiudabot/AIUDA_PACKAGES/arduino_body_serial/src/aiuda_body_serial/script/speed.txt'
prev_angle = 0.0
prev_speed = 0.0


try: 
    body_port = serial.Serial(port=port, baudrate=115200)
    
    aiuda_body_str = [0,0]

    def send_steering_throttle():
        global aiuda_body_str
        global prev_angle, prev_speed
        
        
        # Read the Angle and Speed
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
        
        aiuda_body_str[0] = speed_value
        aiuda_body_str[1] = angle_value
        
        aiuda_body_str = str(aiuda_body_str) + '\n'
        start_sending_body()

    def sending_to_relay_module():
        global aiuda_body_str
        while True:
            body_port.write(aiuda_body_str.encode())
            global stop_threads
            if stop_threads:
                break
            # print("SERIAL THREAD ALIVE")

    def start_sending_body():
        global stop_threads
        global t1
        stop_threads = False
        t1 = threading.Thread(target=send_steering_throttle)
        t1.start()


    def stop_sending_body():
        global stop_threads
        global t1
        stop_threads = True
        t1.join()
except:
    
    aiuda_body_str = [0,0]
    print('***************************ARDUINO BODY NOT CONNECTED*************************')
