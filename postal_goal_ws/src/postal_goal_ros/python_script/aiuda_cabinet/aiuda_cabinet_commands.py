
cabinet_path = '/home/aiudabot/AIUDA_PACKAGES/postal_goal_ws/src/postal_goal_ros/python_script/aiuda_cabinet/cabinet_status_list.txt'


def activate_all_cabinet():
    list_value = [1] * 13


    with open(cabinet_path, 'w') as filehandle:
        for listitem in list_value:
            filehandle.write('%s\n' % listitem)
            
def activate_upper_cabinet():
    
    list_value = [1,1,1,0,0,0,1,1,1,0,0,0,1]
    
    with open(cabinet_path, 'w') as filehandle:
        for listitem in list_value:
            filehandle.write('%s\n' % listitem)
            
def activate_lower_cabinet():
    
    list_value = [0,0,0,1,1,1,0,0,0,1,1,1,1]
    
    with open(cabinet_path, 'w') as filehandle:
        for listitem in list_value:
            filehandle.write('%s\n' % listitem)

def deactivate_all_cabinet():
    list_value = [0] * 13
    
    # Turn On UV Light
    list_value[-1] = 1
    
    with open(cabinet_path, 'w') as filehandle:
        for listitem in list_value:
            filehandle.write('%s\n' % listitem)
    print('Deactivating Cabinet')
            
def activate_slot(slot_number):
    cabinet_relay = [0] * 13
    cabinet_relay[slot_number-1] = 1
    cabinet_relay[-1] = 1
    
    with open(cabinet_path, 'w') as filehandle:
        for listitem in cabinet_relay:
            filehandle.write('%s\n' % listitem)