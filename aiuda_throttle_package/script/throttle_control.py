#!/usr/bin/python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import numpy as np
from roi_color import detect_color
from throttle_update import update_throttle_value

class ThrottleController(object):
    
    def __init__(self):
        
        self.image_pub = rospy.Publisher("/throttle_image",Image)
        
        self.image_sub = rospy.Subscriber("/segnet/overlay",Image, self.camera_callback)
        
        self.bridge_object = CvBridge()
        
    def camera_callback(self,data):
        try:
            cv_image = self.bridge_object.imgmsg_to_cv2(data, desired_encoding="bgr8")
            
            cv_image, speed = detect_color(cv_image)
            
            #update throttle value
            update_throttle_value(speed)
            print(speed)
            
            self.image_pub.publish(self.bridge_object.cv2_to_imgmsg(cv_image, "bgr8"))
            
        except CvBridgeError as e:
            print(e)
        
        
    
def main():
    throttle_object = ThrottleController()
    rospy.init_node('throttle_node', anonymous=True)
    
    try:
        rospy.spin()
    
    except KeyboardInterrupt:
        print('Shutting Down')
        

if __name__ == '__main__':
    main()