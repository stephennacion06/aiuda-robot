import serial
import pynmea2
import os
from aiuda_distribution.aiuda_db_modules import get_info_sms
import time


os.system('sudo chmod 777 /dev/ttyUSB0')
ser = serial.Serial(port='/dev/ttyUSB0', baudrate=9600)
print('Serial Port Opened')

def at_commands(at, at_bytes):
    cmd = at
    ser.write(cmd.encode())
    msg = ser.readline(at_bytes)
    print(msg)

    return msg

at_commands(at="AT\r", at_bytes=64)

def read_gps():
    msg = str(ser.readline())
    if "+GPSRD:$GNGGA" in msg:
        gpmrc = msg
        gpmrc = gpmrc[9:]
        gpmrc = gpmrc[:-5]
        coordinates = pynmea2.parse(gpmrc)
        lat = "{:.6f}".format(float(coordinates.lat)/98.42999071)
        lon = "{:.6f}".format(float(coordinates.lon)/99.67104358)
        # gps_coordinates = (str(lat) + '°' + coordinates.lat_dir + ' '
        #                    + str(lon) + '°' + coordinates.lon_dir)

        gps_coordinates = (str(lat), str(lon))
        if gps_coordinates == None:
            gps_coordinates = ('14.571730', '120.995217')

        return gps_coordinates


def activate_gps():
    at_commands(at="AT+GPSRD=0\r", at_bytes=64)
    at_commands(at="AT+GPS=1\r", at_bytes=64)
    at_commands(at="AT+GPSRD=1\r", at_bytes=64)


def test_gps():
    activate_gps()
    while True:
        print(read_gps())
        
def starting_delivery_sms(telephone_num,name,address,cabinet):
    # #Disable GPS 
    # print('Trying to Disable GPS')
    # at_commands(at="AT\r", at_bytes=64)
    # at_commands(at="AT+GPS=0\r", at_bytes=64)
    # at_commands(at="AT+GPSRD=0\r", at_bytes=64)
    # print('GPS DISABLE')
    
    #Send SMS
    cmd= 'AT+CMGF=1\r'
    ser.write(cmd.encode())
    msg=ser.readline()
    print(msg)

    cmd= 'AT+CMGS="{0}"\r'.format(telephone_num)
    ser.write(cmd.encode())
    msg=ser.readline()
    print(msg)
    cmd = "Hello {0}, this is AI-UDA Robot Delivery. You are allocated to Ayuda Cabinet No.{1} and I will begin delivering it to {2}. Please ready your QR-code for receiving the Ayuda.\r".format(name,cabinet,address)
    ser.write(cmd.encode())
    ser.write(serial.to_bytes([0x1A]))
    msg=ser.readline()
    print(msg)

    # #Activate again GPS
    # at_commands(at="AT+GPS=1\r", at_bytes=64)
    # at_commands(at="AT+GPSRD=1\r", at_bytes=64)
    
def introduction_sms(telephone_num,name,address,cabinet):
    # #Disable GPS 
    # print('Trying to Disable GPS')
    # at_commands(at="AT\r", at_bytes=64)
    # at_commands(at="AT+GPS=0\r", at_bytes=64)
    # at_commands(at="AT+GPSRD=0\r", at_bytes=64)
    # print('GPS DISABLE')
    
    cmd= 'AT+CMGF=1\r'
    ser.write(cmd.encode())

    cmd= 'AT+CMGS="{0}"\r'.format(telephone_num)
    ser.write(cmd.encode())
    # msg=ser.readline()
    # print(msg)
    cmd = "Hello {0}, this is AI-UDA Robot. Please confirm your Address: {1} for Ayuda Delivery by sending a SMS to our developer Andrew Stephen A. Nacion, 09193567298\r".format(name,address)
    ser.write(cmd.encode())
    ser.write(serial.to_bytes([0x1A]))
    
    cmd= 'AT+CMGF=0\r'
    ser.write(cmd.encode())
    
    time.sleep(10)

    


def send_introduction(qrcode_list):
    #Start SMS

    
    for qrcode in qrcode_list:
        info = get_info_sms(qrcode)
        address = info[0][0]
        contact = info[0][1]
        name = info[0][2]
        cabinet_num = info[0][3]
        introduction_sms(telephone_num=contact,name=name,address=address,cabinet=cabinet_num)
        print('SMS SENT')

    
    
    
if __name__ == '__main__':
    
    #Test SMS
    starting_delivery_sms('09193567298','Stephen Nacion','Manila','1')
    
