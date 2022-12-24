import serial
import pynmea2

ser = serial.Serial(port='/dev/ttyUSB0', baudrate=9600)


def at_commands(at, at_bytes):
    cmd = at
    ser.write(cmd.encode())
    msg = ser.readline(at_bytes)
    print(msg)

    return msg


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
