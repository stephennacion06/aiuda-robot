#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import PoseWithCovarianceStamped
from tf.transformations import quaternion_from_euler

postal_x = 0
postal_y = 0
th = 2


def callback(data):
    global postal_x, postal_y
    cur_x = data.pose.position.x
    cur_y = data.pose.position.y
    if (postal_x-th <= cur_x <= postal_x+th) and (postal_x-th <= cur_y <= postal_x+th
    
 
    

    
def compare_location(target_x,target_y):
    global postal_x,postal_y
    postal_x = target_x
    postal_y = target_y
    
    rospy.init_node('check_location')
    location_reached = rospy.Subscriber('orb_slam2_mono/pose', PoseStamped, callback)
    return location_reach
    