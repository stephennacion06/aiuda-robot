#!/usr/bin/env python3
# license removed for brevity

import rospy
from parse_xy import get_postal_xy
# Brings in the SimpleActionClient
import actionlib
# Brings in the .action file and messages used by the move base action
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import PoseStamped
from aiuda_distribution.aiuda_db_modules import *
from qr_code_scan import qr_code_main
from aiuda_gps_sms import starting_delivery_sms, arrived_delivery_sms

status_path = '/home/aiudabot/AIUDA_PACKAGES/postal_goal_ws/src/postal_goal_ros/python_script/delivery_status.txt'

# Waiting Path File
waiting_file_path = '/home/aiudabot/AIUDA_PACKAGES/arduino_body_serial/src/aiuda_body_serial/script/waiting.txt'

# Disable Waiting Mode
waiting_file = open(waiting_file_path, 'w')
waiting_file.write(str(0))
waiting_file.close()

# Speed Path
speed_path = '/home/aiudabot/AIUDA_PACKAGES/arduino_body_serial/src/aiuda_body_serial/script/speed.txt'


# Threshold for Map location
th_x = 0.1
th_y = 1.0




def check_location(goal_x, goal_y):

    pose_msg = rospy.wait_for_message('orb_slam2_mono/pose', PoseStamped)
    cur_x = pose_msg.pose.position.x
    cur_y = pose_msg.pose.position.y
    if (goal_x - th_x <= cur_x <= goal_x + th_x) and (goal_y - th_y <= cur_y <= goal_y + th_y):
        return True
    else:
        return False        

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
    # wait = client.wait_for_result()
   # If the result doesn't arrive, assume the Server is not available
    destination_reached = check_location(postal_x,postal_y)
    return destination_reached

    




# If the python node is executed as main process (sourced directly)
if __name__ == '__main__':

    try:
        f = open(status_path, "w")
        f.write("0,0")
        f.close()
       # Initializes a rospy node to let the SimpleActionClient publish and subscribe
        rospy.init_node('movebase_client_py')
        
        while True:
            
            file = open(status_path,"r")
            
            for line in file:
                fields = line.split(",")
                start_delivery = fields[0]
                select_num = fields[1]
            print(start_delivery,select_num)

            if start_delivery == '1':
                rospy.loginfo("STARTED DELIVERY")

                cabinet_slot_list = [1,7,2,8,3,9,4,10,5,11,6,12]

                for cabinet_num in range(0,int(select_num)):
                    
                    # Restart waiting to 0
                    waiting_file = open(waiting_file_path, 'w')
                    waiting_file.write(str(0))
                    waiting_file.close()
                    
                    
                    #STOP DELIVERY WHEN CANCELLED
                    file = open(status_path,"r")
                    for line in file:
                        fields = line.split(",")
                        start_delivery = fields[0]
                    if start_delivery == '0':
                        break
                    
                    delivery_done =False
                    
                    location, postal_address, contact, name, ayuda, barcode = get_info_cabinet_num(cabinet_slot_list[cabinet_num])
                    print("-----Start delivery to-----")
                    print("Name: ",name)
                    print("Contact Number: ",contact)
                    print("Address", location)
                    
                    # NOTE: Add database update to Arriving
                    arriving_update(cabinet_slot_list[cabinet_num])
                    
                    # NOTE: Add SMS for arriving
                    try:
                        
                        starting_delivery_sms( contact, name, location, cabinet_slot_list[cabinet_num])
                    
                    except Exception as e: 
                        rospy.loginfo(e)
                        rospy.loginfo("GPS and SMS Not Connected")
                    
                    while delivery_done == False:

                        #STOP DELIVERY WHEN CANCELLED
                        file = open(status_path,"r")
                        for line in file:
                            fields = line.split(",")
                            start_delivery = fields[0]
                        if start_delivery == '0':
                            break

                        postal_x,postal_y = get_postal_xy(str(postal_address))
                        
                        #for loop here for number of postal_x,y

                        destination_reached = movebase_client(postal_x,postal_y)
        
                        #Check the Goal_X and Goal_Y
                        
                        if destination_reached:
                            
                            loginfo_str = "Succesfully reached destination " + str(cabinet_num) +"!"
                            rospy.loginfo(loginfo_str)
                            
                            # NOTE: Add database update arrived
                            arrived_update(cabinet_slot_list[cabinet_num])
                            
                            # NOTE: Add SMS Here for arrived
                            try:
                                arrived_delivery_sms(contact, name, location, cabinet_slot_list[cabinet_num])
                            
                            except Exception as e: 
                                
                                print(e)
                                rospy.loginfo(e)
                                print("GPS and SMS Not Connected")
                            
                            # Set Waiting Mode to True
                            waiting_file = open(waiting_file_path, 'w')
                            waiting_file.write(str(1))
                            waiting_file.close()
                            
                            # Stop the Etrike
                            speed_file = open(speed_path, 'w')
                            speed_file.write(str(0))
                            speed_file.close()
                            
                            # NOTE: ADD QRCODE SCANNING HERE
                            try:
                                delivery_status = qr_code_main(cabinet_slot_list[cabinet_num])
                            
                            except Exception as e:
                                delivery_status = "Failed" 
                                rospy.loginfo(e)
                                rospy.loginfo("ERROR RUNNING QR CODE SCANNER")
                            
                            # NOTE: Add database update if Done or Failed and Update the Slot number to 0
                            done_or_fail_update(cabinet_slot_list[cabinet_num], delivery_status)
                            
                            delivery_done = True
                
                f = open(status_path, "w")
                print("DELIVERY IS DONE")
                write_text = "{0},{1}".format(str(0),str(0))
                f.write(write_text)
                f.close()

    except rospy.ROSInterruptException:
        f = open(status_path, "w")
        write_text = "{0},{1}".format(str(0),str(0))
        f.write(write_text)
        f.close()
        rospy.loginfo("Navigation test finished.")