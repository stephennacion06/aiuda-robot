import camera_stream
from flask import Flask, render_template, request, redirect, url_for, Response
from camera_stream import gen_frames
# AIUDA DATABASE
from aiuda_distribution.aiuda_db_modules import get_name_database, \
    get_qrcode_database, postal_codes_with_rfid, get_status_database, \
    ayuda_slot_assignment_algo, update_status_delivery, get_selected_name, \
    cancel_status_delivery
# GPS MODULE
try:
    from aiuda_gps import activate_gps, read_gps
    gps_ready = True
except:
    gps_ready = False
    print("GPS NOT READY OR CONNECTED")
# SERIAL CONTROL MODULE
try:
    from serial_body import send_serial_body
    serial_body_status = True
    speed = 0
    angle = 45
except:
    serial_body_status = False
    print("SERIAL TO AIUDA BODY NOT READY OR CONNECTED")
    speed = 0
    angle = 45


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


@app.route('/video_feed')
def video_feed():
    # Video streaming route. Put this in the src attribute of an img tag
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/manualcontrol')
def manual_control():
    """Video streaming home page."""
    return render_template('remote_control.html')


@app.route('/left_side')
def left_side():
    global speed, angle
    angle -= 1
    if angle < 0:
        angle = 0
    print(speed, angle)
    if serial_body_status == True:
        send_serial_body(speed=speed, angle=angle)
    return 'true'


@app.route('/right_side')
def right_side():
    global speed, angle
    data1 = "RIGHT"
    angle += 1
    if angle > 90:
        angle = 90
    print(speed, angle)
    if serial_body_status == True:
        send_serial_body(speed=speed, angle=angle)
    return 'true'


@app.route('/up_side')
def up_side():
    global speed, angle
    data1 = "FORWARD"
    speed = 4
    print(speed, angle)
    if serial_body_status == True:
        send_serial_body(speed=speed, angle=angle)
    return 'true'


@app.route('/down_side')
def down_side():
    global speed, angle
    speed = -4
    print(speed, angle)
    if serial_body_status == True:
        send_serial_body(speed=speed, angle=angle)
    return 'true'


@app.route('/stop')
def stop():
    global speed, angle
    speed = 0
    print(speed, angle)
    if serial_body_status == True:
        send_serial_body(speed=speed, angle=angle)
    return 'true'
########### MANUAL CONTROL AND VIDEO CAPTURE ####################

########### GPS SHOW LOCATION ####################


@app.route('/location', methods=['GET', 'POST'])
def show_location():
    if gps_ready == True:
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

    if delivery_started:
        return redirect(url_for("automated_monitoring"))
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

                start_delivery = 1
                f = open("delivery_status.txt", "w")
                write_text = "{0},{1}".format(start_delivery, select_num)
                f.write(write_text)
                f.close()

                delivery_started = True
                return redirect(url_for("automated_monitoring"))

        # RENDER AYUDA ASSIGNMENT PAGE
        return render_template("automated_distribution.html",
                               len=len(name_list),
                               name_list=name_list,
                               qrcode_list=qrcode_value,
                               status_delivery=status_delivery,
                               status_list=status_value,
                               )


@app.route('/automatedMonitoring', methods=['GET', 'POST'])
def automated_monitoring():
    global name_length_monitoring, name_list_monitoring,\
        status_delivery_monitoring, status_list_monitoring
    global delivery_started

    # Update Status Before Rendering
    status_list_monitoring = get_status_database(name_list_monitoring)

    if request.method == 'POST':
        # make status 'Cancelled' when the resident has assigned cabinet num
        cancel_status_delivery()
        delivery_started = False
        return redirect(url_for("automated_distribution"))

    return render_template('automated_delivery_mode.html',
                           length=name_length_monitoring,
                           name_list=name_list_monitoring,
                           status_delivery=status_delivery_monitoring,
                           status_list=status_list_monitoring
                           )


if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=True)
