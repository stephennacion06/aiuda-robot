import camera_stream
from flask import Flask, render_template, request, redirect, url_for, Response
from camera_stream import gen_frames



# AIUDA DATABASE
from aiuda_distribution.aiuda_db_modules import get_name_database, \
    get_qrcode_database, postal_codes_with_rfid, get_status_database, \
    ayuda_slot_assignment_algo, update_status_delivery, get_selected_name, \
    cancel_status_delivery, clear_ayuda_cabinet_num

# GPS MODULE
try:
    from aiuda_gps_sms import activate_gps, read_gps, send_introduction
    gps_ready = True
except:
    gps_ready = False
    print("GPS NOT READY OR CONNECTED")
# gps_ready = False

# SERIAL CONTROL MODULE
try:
    from serial_body import send_speed_body, send_angle_body, activate_manual_control, disable_manual_control
    serial_body_status = True
    speed = 0.0
    angle = 0.0
except:
    serial_body_status = False
    print("SERIAL TO AIUDA BODY NOT READY OR CONNECTED")
    speed = 0.0
    angle = 0.0



# SET to ZERO SPEED AND ANGLE
angle_path = '/home/aiudabot/AIUDA_PACKAGES/arduino_body_serial/src/aiuda_body_serial/script/angle.txt'
speed_path = '/home/aiudabot/AIUDA_PACKAGES/arduino_body_serial/src/aiuda_body_serial/script/speed.txt'
angle_file = open(angle_path, 'w')
angle_file.write(str(0))
angle_file.close()

speed_file = open(speed_path, 'w')
speed_file.write(str(0))
speed_file.close()


# AIUDA CABINET MODULE
from aiuda_cabinet.aiuda_cabinet_commands import activate_lower_cabinet,activate_upper_cabinet, deactivate_all_cabinet
delivery_status_path = '/home/aiudabot/AIUDA_PACKAGES/postal_goal_ws/src/postal_goal_ros/python_script/delivery_status.txt'

# DEACTIVATE ALL CABINET BEFORE STARTING
deactivate_all_cabinet()
clear_ayuda_cabinet_num()

app = Flask(__name__)

########### LOGIN PAGE ####################
admin_account = ["admin_aiuda", "1234"]


@app.route('/', methods=['GET', 'POST'])
def login():

    if request.method == "POST":
        request_account = [request.form["username"], request.form["password"]]
        if admin_account == request_account:
            print("Login successfully")
            return redirect(url_for('menu'))
        else:
            print("INVALID ACCOUNT")

    return render_template('login_form.html')
########### LOGIN PAGE ####################


########### MENU PAGE ####################
@app.route('/menu')
def menu():
    return render_template('home_page.html')
########### MENU PAGE ####################

########### MANUAL CONTROL AND VIDEO CAPTURE ####################


# @app.route('/video_feed')
# def video_feed():
#     # Video streaming route. Put this in the src attribute of an img tag
#     return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/manualcontrol')
def manual_control():
    """Video streaming home page."""
    activate_manual_control()
    
    return render_template('remote_control.html')


@app.route('/left_side')
def left_side():
    angle = -5
    if serial_body_status == True:
        send_angle_body(angle=angle)
    return 'true'


@app.route('/right_side')
def right_side():
    angle = 5
    if serial_body_status == True:
        send_angle_body(angle=angle)
    return 'true'


@app.route('/up_side')
def up_side():
    speed = 2.0
    if serial_body_status == True:
        send_speed_body(speed=speed)
    return 'true'


@app.route('/down_side')
def down_side():
    speed = -2.0
    if serial_body_status == True:
        send_speed_body(speed=speed)
    return 'true'


@app.route('/stop')
def stop():
    speed = 0.0
    if serial_body_status == True:
        send_speed_body(speed=speed)
    return 'true'
########### MANUAL CONTROL AND VIDEO CAPTURE ####################

########### GPS SHOW LOCATION ####################


@app.route('/location', methods=['GET', 'POST'])
def show_location():
    if gps_ready == True:
        print("GPS READY!")
        gps_coordinates = read_gps()
        if gps_coordinates == None:
            gps_coordinates = ('14.571730', '120.995217')
        print(gps_coordinates)
        # show the form, it wasn't submitted
        return render_template('gps_location.html', gps_coordinates=gps_coordinates)
    else:
        return 'GPS NOT CONNECTED!'


########### AUTOMATED LOAD DISTRIBUTION ####################
start_delivery = 0
select_num = 0

# For AYUDA Monitoring
name_length_monitoring = 0
name_list_monitoring = []
status_delivery_monitoring = "Waiting"
status_list_monitoring = []
delivery_started = False


@app.route('/automatedLoadDistribution', methods=['GET', 'POST'])
def automated_distribution():
    global start_delivery, select_num

    # For AYUDA monitoring
    global name_length_monitoring, name_list_monitoring,\
        status_delivery_monitoring, status_list_monitoring
    global delivery_started

    #SET MANUAL CONTROL TO FALSE
    disable_manual_control()
    
    if delivery_started:
        return redirect(url_for("automated_loading"))
    else:
        name_length_monitoring = 0
        name_list_monitoring = []
        status_delivery_monitoring = "Waiting"
        status_list_monitoring = []

        name_list = get_name_database()
        
        qrcode_value = get_qrcode_database(name_list)
        status_value = get_status_database(name_list)

        status_delivery = "Waiting"
        if request.method == 'POST':
            qr_code_list = request.form.getlist('mycheckbox')
            select_num = len(qr_code_list)
            if select_num > 12:
                status_delivery = "Select 1-12 only"
            elif select_num == 0:
                status_delivery = "Select 1-12"
            else:
                status_delivery = "Delivering to {0} Family".format(
                    str(select_num))

                update_status_delivery(qr_code_list)
                
                # Filter the Name and Status in Automated Monitoring Mode
                selected_name = get_selected_name(qr_code_list)
                status_value_list = get_status_database(selected_name)

                # Global Variable Assignment for AIUDA Monitoring
                name_length_monitoring = select_num
                name_list_monitoring = selected_name
                status_delivery_monitoring = status_delivery
                status_list_monitoring = status_value_list

                # POSTAL ASSIGNMENT ALGO
                postal_code_parsed = postal_codes_with_rfid(qr_code_list)

                ayuda_slot_assignment_algo(postal_code_parsed, qr_code_list)

                #Activate All Cabinet
                # activate_all_cabinet()

                
                # Initial SMS for delivery
                if gps_ready:
                    send_introduction(qr_code_list)
                    
                
                
                return redirect(url_for("automated_loading"))

        # RENDER AYUDA ASSIGNMENT PAGE
        return render_template("automated_assignment.html",
                               len=len(name_list),
                               name_list=name_list,
                               qrcode_list=qrcode_value,
                               status_delivery=status_delivery,
                               status_list=status_value,
                               )

@app.route('/automatedLoading', methods=['GET', 'POST'])
def automated_loading():
    global name_length_monitoring, name_list_monitoring,\
        status_delivery_monitoring, status_list_monitoring
    global delivery_started
    global select_num
    
    # Update Status Before Rendering
    status_list_monitoring = get_status_database(name_list_monitoring)
    
    #SET MANUAL CONTROL TO FALSE
    disable_manual_control()
    if delivery_started == False:
        
        
        if request.method == 'POST':
            
            if request.form['submit_button'] == 'cabinet_1':
                activate_upper_cabinet()
            
            elif request.form['submit_button'] == 'cabinet_2':
                activate_lower_cabinet()
            
            elif request.form['submit_button'] == 'start':
                    
                #Lock all cabinet before starting delivery
                deactivate_all_cabinet()
                
                start_delivery = 1
                
                f = open(delivery_status_path, "w")
                write_text = "{0},{1}".format(start_delivery, select_num)
                f.write(write_text)
                f.close()

                delivery_started = True
                return redirect(url_for("automated_monitoring"))

        
        return render_template('automated_loading.html',
                            length=name_length_monitoring,
                            name_list=name_list_monitoring,
                            status_delivery=status_delivery_monitoring,
                            status_list=status_list_monitoring
                            )
    else:
        return redirect(url_for("automated_monitoring"))


@app.route('/automatedMonitoring', methods=['GET', 'POST'])
def automated_monitoring():
    global name_length_monitoring, name_list_monitoring,\
        status_delivery_monitoring, status_list_monitoring
    global delivery_started
    global select_num
    
    # Update Status Before Rendering
    status_list_monitoring = get_status_database(name_list_monitoring)
    
    #SET MANUAL CONTROL TO FALSE
    disable_manual_control()

    if request.method == 'POST':
        
        
        # make status 'Cancelled' when the resident has assigned cabinet num
        
        cancel_status_delivery()
        clear_ayuda_cabinet_num()
        delivery_started = False
        
        f = open(delivery_status_path, "w")
        write_text = "{0},{1}".format(0, 0)
        f.write(write_text)
        f.close()
        
        
        return redirect(url_for("automated_distribution"))

    
    return render_template('automated_monitoring.html',
                           length=name_length_monitoring,
                           name_list=name_list_monitoring,
                           status_delivery=status_delivery_monitoring,
                           status_list=status_list_monitoring
                           )

@app.route('/automatedRemote', methods=['GET', 'POST'])
def automated_remote():
    global name_length_monitoring, name_list_monitoring,\
        status_delivery_monitoring, status_list_monitoring
    global delivery_started
    global select_num
    
    # Update Status Before Rendering
    status_list_monitoring = get_status_database(name_list_monitoring)
    
    #SET MANUAL CONTROL TO FALSE
    disable_manual_control()
    
    return render_template('automated_remote_control.html',
                           length=name_length_monitoring,
                           name_list=name_list_monitoring,
                           status_delivery=status_delivery_monitoring,
                           status_list=status_list_monitoring
                           )

if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=False)
