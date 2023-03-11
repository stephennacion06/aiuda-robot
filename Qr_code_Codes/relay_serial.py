import serial
import time
import threading
import os

os.system('sudo chmod 777 /dev/ttyUSB0')
relay_module_serial = serial.Serial(port='/dev/ttyUSB0', baudrate=9600)
# relay_module_serial.flush()

sending_str = str([0,0,0,0,0,0,0,0,0,0,0,0,0]) + '\n'

def open_ayuda_slot(slot_number):
    global sending_str
    cabinet_relay = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    cabinet_relay[slot_number-1] = 1
    cabinet_relay[-1] = 1
    sending_str = str(cabinet_relay) + '\n'
    start_sending_relay_module()
    #print(str(cabinet_relay))

def sending_to_relay_module():
    global sending_str
    while True:
        relay_module_serial.write(sending_str.encode())
        global stop_threads
        if stop_threads:
            break
        # print("SERIAL THREAD ALIVE")
def close_relay_module():
    global sending_str
    sending_str = str([0,0,0,0,0,0,0,0,0,0,0,0,0]) + '\n'

def start_sending_relay_module():
    global stop_threads
    global t1
    stop_threads = False
    t1 = threading.Thread(target=sending_to_relay_module)
    t1.start()


def stop_sending_relay_module():
    global stop_threads
    global t1
    stop_threads = True
    t1.join()
