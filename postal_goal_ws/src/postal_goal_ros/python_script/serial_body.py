angle_path = '/home/aiudabot/AIUDA_PACKAGES/arduino_body_serial/src/aiuda_body_serial/script/angle.txt'
speed_path = '/home/aiudabot/AIUDA_PACKAGES/arduino_body_serial/src/aiuda_body_serial/script/speed.txt'
manual_path = '/home/aiudabot/AIUDA_PACKAGES/arduino_body_serial/src/aiuda_body_serial/script/manual.txt'

prev_angle = 0.0



def send_angle_body(angle):
    global prev_angle
    
    angle_file = open(angle_path, 'r')
    
    #If angle value is empty use the prev_value
    try:
        angle_value = float(angle_file.read())
        prev_angle = angle_value
    except:
        angle_value = prev_angle
    
    angle_value += angle
    #update angle
    angle_file = open(angle_path, 'w')
    angle_file.write(str(angle_value))
    angle_file.close()
    
    #update manual
    manual_file = open(manual_path, 'w')
    manual_file.write(str(1))
    manual_file.close()
    
def send_speed_body(speed):    
    #update speed
    speed_file = open(speed_path, 'w')
    speed_file.write(str(speed))
    speed_file.close()
    
    #update manual
    manual_file = open(manual_path, 'w')
    manual_file.write(str(1))
    manual_file.close()

    
def activate_manual_control():
    #update manual
    manual_file = open(manual_path, 'w')
    manual_file.write(str(1))
    manual_file.close()

def disable_manual_control():
    #update manual
    manual_file = open(manual_path, 'w')
    manual_file.write(str(0))
    manual_file.close()
