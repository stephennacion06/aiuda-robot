import cv2
from pyzbar import pyzbar
from aiuda_db_modules import find_qr_code
import threading
import time 

end_scan = False
qr_detected = False

timer_done = False
waiting_time = 5
timer_int = 0
t_t = None

waiting_max_minutes = 1
waiting_time_reached = False
timer_waiting_int = 0

def ck():

    global timer_int
    global timer_done
    global t_t

    t_t = threading.Timer(1, ck)
    t_t.start()
    print("Adding time! ",timer_int)
    timer_int += 1
    if timer_int >= waiting_time:
        timer_done = True
        t_t.cancel()
        print("THRESHOLD TIME DONE!")
    else:
         timer_done = False
    #print('Threshold Timer',timer_int)


def waiting_timer():
    # FUNCTION FOR WAITING TIME
    
    global waiting_max_minutes
    global waiting_time_reached
    global timer_waiting_int
    global w_t

    w_t = threading.Timer(1, waiting_timer)
    w_t.start()
    timer_waiting_int += 1
    if timer_waiting_int >= (waiting_max_minutes*60):
        waiting_time_reached = True
        w_t.cancel()
        print("WAITING TIME DONE!")
    else:
         waiting_time_reached = False
    #print('Waiting Timer: ',timer_waiting_int)



def read_barcodes(frame, slot_qrcode_check):

    barcodes = pyzbar.decode(frame)
    barcode_info = ""

    global timer_done
    global timer_int
    global t_t
    global end_scan
    global qr_detected 
    
    for barcode in barcodes:
        x, y , w, h = barcode.rect

        barcode_info = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)

        font = cv2.FONT_HERSHEY_PLAIN
        cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 3.0, (255, 0, 0), 5)

    if barcode_info == slot_qrcode_check:

        # timer_int = 0
        # ck()
        qr_detected = True
        if t_t is None:
            print("True NONE")
            ck()
            w_t.cancel()
            
            
        #4 thread relay activate which slot to open

        if timer_done == True:
            end_scan = True
            
        # else:
        #     t_t.cancel()
        #     ck()
        #     timer_int = 0
    
    # 2 check if slot_qr is equal to barcode_info return qr_detected = True
    # if slot_qr is equal to barcode_info and timer_done is True return end_scan = True else false
    return frame, qr_detected, end_scan


def gstreamer_pipeline(
    sensor_id=0,
    sensor_mode=3,
    capture_width=640,
    capture_height=480,
    display_width=640,
    display_height=480,
    framerate=30,
    flip_method=0,
):
    return (
        "nvarguscamerasrc sensor-id=%d sensor-mode=%d ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, "
        "format=(string)NV12, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            sensor_id,
            sensor_mode,
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )

# GStreamer Pipeline to access the Web CAM
def open_cam_usb(dev, width, height):
    # We want to set width and height here, otherwise we could just do:
    #     return cv2.VideoCapture(dev)
    gst_str = ('v4l2src device=/dev/video{} ! '
               'video/x-raw, width=(int){}, height=(int){} ! '
               'videoconvert ! appsink').format(dev, width, height)
    return gst_str

GSTREAMER_PIPELINE = open_cam_usb(0,640,480)


def restart_qr_params():
    global end_scan, qr_detected, timer_done, waiting_time, timer_int, t_t
    global waiting_max_minutes, waiting_time_reached, timer_waiting_int

    end_scan = False
    qr_detected = False

    timer_done = False
    waiting_time = 5
    timer_int = 0
    t_t = None

    waiting_max_minutes = 5
    waiting_time_reached = False
    timer_waiting_int = 0

def qr_code_main(slot_num):
    try:
        global t_t
        global timer_int 
        global w_t
        
        global waiting_time_reached

        waiting_timer()

        #1 find_qr_code_to_scan in database (inside aiuda_db_modules.py) slot_qr = find_qr_code(slot number)
        slot_qr = find_qr_code(slot_number=slot_num)
        
        # cap = cv2.VideoCapture(gstreamer_pipeline(), cv2.CAP_GSTREAMER)
        cap = cv2.VideoCapture(GSTREAMER_PIPELINE, cv2.CAP_GSTREAMER)
        ret,frame = cap.read()

        while ret:
            ret, frame = cap.read()

            frame, bool_detected_qrcode, bool_end_scan = read_barcodes(frame, slot_qr)
            # print('Threshold Timer',timer_int,bool_end_scan)
            
            cv2.imshow('AI-UDA QR-code Reader', frame)

            if bool_detected_qrcode == True:
                    
                # NOTE: create a function for open_ayuda_slot in ayuda_container_commands
                pass
                



            #5  if cv2.waitKey(1) & 0xFF == 27 OR end_scan = True OR 
            # max_waiting_time = True return or break return status
            
            #6 Run max_waiting_timer if 5 minutes has passed max_waiting_time = True
            if (cv2.waitKey(1) & 0xFF == 27) or (bool_end_scan == True):
                try:
                    # NOTE: Close Relay Module Here
                    #Restart All Process
                    cap.release()
                    cv2.destroyAllWindows()
                    restart_qr_params()
                    w_t.cancel()
                    t_t.cancel()
                    return "DONE"
                except:
                    print('Error on Restarting Parametenrs')
        
            if (waiting_time_reached):
                try:
                    # NOTE: Close Relay Module Here
                    #Restart All Process
                    cap.release()
                    cv2.destroyAllWindows()
                    restart_qr_params()
                    print('Waiting time Reached!')
                    return "FAILED"
                except:
                    print('Error on Restarting Parametenrs')
    except:
        return "FAILED"

qr_waiting = qr_code_main(1)
print(qr_waiting)