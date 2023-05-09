import serial
import os
from serial.tools import list_ports

device_list = list_ports.comports()

# Cabinet MCU Vendor ID and Product ID
aiudaCabinetVid = 1659
aiudaCabinetPid = 8963
port = None

for device in device_list:
    if(device.vid != None or device.pid != None):
        print("Initialize Aiuda Cabinet connection")
        if ( device.vid == aiudaCabinetVid ) and ( device.pid == aiudaCabinetPid ):
            port = device.device
            print("Serial Port Selected: ", port)
            osCmd = "sudo chmod 666 " + port
            os.system(osCmd)
            print("Sucessful setting " + osCmd)
            break

try:
    relay_module_serial = serial.Serial(port=port, baudrate=9600)
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
    
    cabinet_list = str(cabinet_list) + '\n'
    
    if serial_ready:
        
        print(cabinet_list)
        relay_module_serial.write(cabinet_list.encode())