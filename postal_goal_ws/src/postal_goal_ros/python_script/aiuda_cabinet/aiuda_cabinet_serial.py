import serial
import os

try:
    os.system('sudo chmod 777 /dev/ttyUSB0')
    
    relay_module_serial = serial.Serial(port='/dev/ttyUSB0', baudrate=9600)
    
    serial_ready = True
except Exception as e: 
    serial_ready = False
    print(e)

cabinet_path = '/home/aiudabot/AIUDA_PACKAGES/postal_goal_ws/src/postal_goal_ros/python_script/aiuda_cabinet/cabinet_status_list.txt'

while True:
    # define an empty list
    cabinet_list = []
    # open file and read the content in a list
    with open(cabinet_path, 'r') as filehandle:
        for line in filehandle:
            # remove linebreak which is the last character of the string
            cabinet_slot = line[:-1]

            # add item to the list
            cabinet_list.append(int(cabinet_slot))
    
    print(cabinet_list)
    
    cabinet_list = str(cabinet_list) + '\n'
    
    if serial_ready:
        
        relay_module_serial.write(cabinet_list.encode())