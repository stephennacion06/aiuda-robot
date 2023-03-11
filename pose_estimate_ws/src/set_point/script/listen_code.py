#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseStamped

def callback(data):
    print data
    variable_x = data.pose.position.x
    rospy.loginfo(rospy.get_caller_id() + 'I heard %f', variable_x)

def listener():
    rospy.init_node('listener', anonymous=False)
    rospy.Subscriber('orb_slam2_mono/pose', PoseStamped, callback)
    # spin() simply keeps python from exiting until this node is stopped
    print PoseStamped
    rospy.spin()

if __name__ == '__main__':
    listener()