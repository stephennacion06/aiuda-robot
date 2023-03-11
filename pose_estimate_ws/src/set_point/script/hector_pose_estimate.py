#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import PoseWithCovarianceStamped
from tf.transformations import quaternion_from_euler



def callback(data):
    global checkpoint
    global pub
    
    
    
    checkpoint.pose.pose.position.x = data.pose.position.x
    checkpoint.pose.pose.position.y = data.pose.position.y
    checkpoint.pose.pose.position.z = data.pose.position.z
    checkpoint.header.frame_id = data.header.frame_id
    print checkpoint.header.frame_id
    [x,y,z,w]=quaternion_from_euler(0.0,0.0,0.0)
    checkpoint.pose.pose.orientation.x = data.pose.orientation.x
    checkpoint.pose.pose.orientation.y = data.pose.orientation.y
    checkpoint.pose.pose.orientation.z = data.pose.orientation.z
    checkpoint.pose.pose.orientation.w = data.pose.orientation.w

    pub.publish(checkpoint)

    
def listener():
    global pub
    global checkpoint
    rospy.init_node('init_pos')
    rospy.Subscriber('orb_slam2_mono/pose', PoseStamped, callback)
    pub = rospy.Publisher('/initialpose', PoseWithCovarianceStamped, queue_size = 10)
    checkpoint = PoseWithCovarianceStamped()
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()