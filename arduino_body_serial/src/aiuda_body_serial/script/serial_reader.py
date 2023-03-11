manual_path = '/home/aiudabot/AIUDA_PACKAGES/arduino_body_serial/src/aiuda_body_serial/script/manual.txt'
prev_manual = 0

angle_path = '/home/aiudabot/AIUDA_PACKAGES/arduino_body_serial/src/aiuda_body_serial/script/angle.txt'
speed_path = '/home/aiudabot/AIUDA_PACKAGES/arduino_body_serial/src/aiuda_body_serial/script/speed.txt'
prev_angle = 0.0
prev_speed = 0.0

while True:
    manual_file = open(manual_path, 'r')
    angle_file = open(angle_path, 'r')
    speed_file = open(speed_path, 'r')
    
    #If manual value is empty use the prev_value
    try:
        manual_value = int(manual_file.read())
        prev_manual = manual_value
    except:
        manual_value = prev_manual
    
    #If Angle value is empty use the prev_value
    try:
        angle_value = float(angle_file.read())
        prev_angle = angle_value
    except:
        angle_value = prev_angle
    
    #If Speed value is empty use the prev_value
    try:
        speed_value = float(speed_file.read())
        prev_speed = speed_value
    except:
        speed_value = prev_speed
    
    output_str = 'SENDING TO AIUDA BODY: Speed = {0}, Angle = {1}, Manual = {2}'.format(speed_value, angle_value, manual_value)
    
    print(output_str)