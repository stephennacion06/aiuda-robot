# Speed and Manual Parameters
speed_path = '/home/aiudabot/AIUDA_PACKAGES/arduino_body_serial/src/aiuda_body_serial/script/speed.txt'
manual_path = '/home/aiudabot/AIUDA_PACKAGES/arduino_body_serial/src/aiuda_body_serial/script/manual.txt'
prev_manual = 0


def update_throttle_value(new_speed):
    global prev_manual
    # Read First Manual to check if manual is activated
    manual_file = open(manual_path, 'r')
    
    #If manual value is empty use the prev_value
    try:
        manual_value = int(manual_file.read())
        prev_manual = manual_value
    except:
        manual_value = prev_manual

    if manual_value == 0:
        #Update speed.txt 
        speed_file = open(speed_path, 'w')
        speed_file.write(str(new_speed))
        speed_file.close()

    