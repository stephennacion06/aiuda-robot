from flask import Flask, render_template, request
from aiuda_db_modules import get_name_database, get_qrcode_database, postal_codes_with_rfid, ayuda_slot_assignment_algo

app = Flask(__name__)

name_list = get_name_database()
qrcode_value = get_qrcode_database(name_list)

start_delivery = 0
select_num = 0
@app.route('/', methods=['GET', 'POST'])

def index():
    global name_list
    global qrcode_value
    global start_delivery
    global select_num
    status_delivery = "Waiting"
    if request.method == 'POST':
        qr_code_list = request.form.getlist('mycheckbox')
        select_num = len(qr_code_list)
        if select_num > 12:
            status_delivery = "Please select 1-12 Residents only"
        else:
            status_delivery = "Starting Delivery to {0} Residents!".format(str(select_num))
            #print(qr_code_list)
            postal_code_parsed = postal_codes_with_rfid(qr_code_list)
            #print(postal_code_parsed)
            ayuda_slot_assignment_algo(postal_code_parsed, qr_code_list)
            start_delivery = 1
            f = open("delivery_status.txt", "w")
            write_text = "{0},{1}".format(start_delivery,select_num)
            f.write(write_text)
            f.close()


    return render_template("index.html",
                           len=len(name_list),
                           name_list = name_list,
                           qrcode_list = qrcode_value,
                           status_delivery = status_delivery
                           )


app.run(debug=True, port=5001)
