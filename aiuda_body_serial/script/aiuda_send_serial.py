#!/usr/bin/env python

import rospy
from nav_msgs.msg import Path
from tf.transformations import euler_from_quaternion
from std_msgs.msg import String
#import arduino body serial connection
try:
    from arduino_serial import  start_sending_body, stop_sending_body
except:
    print("ARDUINO MEGA NOT CONNECTED!")


angle_path = '/home/aiudabot/AIUDA_PACKAGES/arduino_body_serial/src/aiuda_body_serial/script/angle.txt'
manual_path = '/home/aiudabot/AIUDA_PACKAGES/arduino_body_serial/src/aiuda_body_serial/script/manual.txt'
prev_manual = 0

def update_steering(data):
    global pub
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
        angle = data.poses[0]
        quaternion = (
        angle.pose.orientation.x,
        angle.pose.orientation.y,
        angle.pose.orientation.z,
        angle.pose.orientation.w)
        euler = euler_from_quaternion(quaternion)
        
        yaw = euler[2]
        
        #Update angle.txt 
        angle_file = open(angle_path, 'w')
        angle_file.write(str(yaw))
        angle_file.close()

    


def listener():
    global pub

    try:
        start_sending_body()
    except:
        print('Failed to start Serial Communication')
    
    rospy.init_node('arduino_mega_serial')
    
    rospy.Subscriber('/move_base/DWAPlannerROS/global_plan', Path, update_steering)
    
    pub = rospy.Publisher('/arduino_serial_str', String, queue_size = 10)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
    
    try:
        stop_sending_body()
    except:
        print('Failed to stop Serial Communication')
    
    

if __name__ == '__main__':
    listener()