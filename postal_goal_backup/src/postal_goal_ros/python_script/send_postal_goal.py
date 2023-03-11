#!/usr/bin/env python3
# license removed for brevity

import rospy
from parse_xy import get_postal_xy
# Brings in the SimpleActionClient
import actionlib
# Brings in the .action file and messages used by the move base action
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

from aiuda_db_modules import *

def movebase_client(target_x, target_y):

   # Create an action client called "move_base" with action definition file "MoveBaseAction"
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
 
   # Waits until the action server has started up and started listening for goals.
    client.wait_for_server()

   # Creates a new goal with the MoveBaseGoal constructor
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
   # Move 0.5 meters forward along the x axis of the "map" coordinate frame 
    goal.target_pose.pose.position.x = target_x
    goal.target_pose.pose.position.y = target_y

   # No rotation of the mobile base frame w.r.t. map frame
    goal.target_pose.pose.orientation.w = 1.0

   # Sends the goal to the action server.
    client.send_goal(goal)
   # Waits for the server to finish performing the action.
    wait = client.wait_for_result()
   # If the result doesn't arrive, assume the Server is not available
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
    # Result of executing the action
        return client.get_result()


# If the python node is executed as main process (sourced directly)
if __name__ == '__main__':
    try:
        f = open("delivery_status.txt", "w")
        f.write("0,0")
        f.close()
       # Initializes a rospy node to let the SimpleActionClient publish and subscribe
        rospy.init_node('movebase_client_py')
        while True:
            file = open("delivery_status.txt","r")

            for line in file:
                fields = line.split(",")
                start_delivery = fields[0]
                select_num = fields[1]

            print(start_delivery, select_num)

            if start_delivery == '1':
                cabinet_slot_list = [1,7,2,8,3,9,4,10,5,11,6,12]
                for cabinet_num in range(0,int(select_num)):
                    delivery_done =False
                    location, postal_address, contact, name, ayuda, barcode = get_info_cabinet_num(cabinet_slot_list[cabinet_num])
                    print("-----Start delivery to-----")
                    print("Name: ",name)
                    print("Contact Number: ",contact)
                    print("Address", location)
                    
                    while delivery_done == False:
                        postal_x,postal_y = get_postal_xy(str(postal_address))
                        #for loop here for number of postal_x,y
                        result = movebase_client(postal_x,postal_y)
                        if result:
                            loginfo_str = "Succesfully reached destination " + str(cabinet_num) +"!"
                            rospy.loginfo(loginfo_str)
                            delivery_done = True
                f = open("delivery_status.txt", "w")
                print("DELIVERY IS DONE")
                write_text = "{0},{1}".format(str(0),str(0))
                f.write(write_text)
                f.close()
        

    except rospy.ROSInterruptException:
        f = open("delivery_status.txt", "w")
        write_text = "{0},{1}".format(str(0),str(0))
        f.write(write_text)
        f.close()
        rospy.loginfo("Navigation test finished.")