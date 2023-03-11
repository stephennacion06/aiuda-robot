import sqlite3
import re


def insertVaribleIntoTable(location, contact, name, ayuda, barcode, cabinet_num):
    try:
        sqliteConnection = sqlite3.connect('barangay_residents.db')
        cursor = sqliteConnection.cursor()
        # print("Connected to SQLite")

        sqlite_insert_with_param = """INSERT INTO Residents
                          (location, contact, name, ayuda, barcode, cabinet_num)
                          VALUES (?,?,?,?,?,?);"""

        data_tuple = (location, contact, name, ayuda, barcode, cabinet_num)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        # print("Python Variables inserted successfully into SqliteDb_developers table")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")


def get_name_database():
    try:
        sqliteConnection = sqlite3.connect('barangay_residents.db')
        sqliteConnection.row_factory = lambda cursor, row: row[0]
        cursor = sqliteConnection.cursor()
        # print("Connected to SQLite")

        cursor.execute("SELECT name FROM Residents ORDER BY name ASC")
        results = cursor.fetchall()
        #print(results)

        cursor.close()
        return results

    except sqlite3.Error as error:
        print("Failed to check database", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()


def get_qrcode_database(name_list):
    try:
        qrcode_list_sorted = []
        sqliteConnection = sqlite3.connect('barangay_residents.db')
        sqliteConnection.row_factory = lambda cursor, row: row[0]
        cursor = sqliteConnection.cursor()

        for name in name_list:
            cursor.execute("SELECT barcode FROM Residents WHERE name IN ('{0}');".format(name))
            qrcode_result = cursor.fetchall()[0]
            qrcode_list_sorted.append(qrcode_result)
        cursor.close()

        #print(qrcode_list_sorted)
        return qrcode_list_sorted

    except sqlite3.Error as error:
        print("Failed to check database", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()


def postal_codes_with_rfid(rfid_list):
    postal_codes_list = []
    sqliteConnection = sqlite3.connect('barangay_residents.db')
    sqliteConnection.row_factory = lambda cursor, row: row[0]
    cursor = sqliteConnection.cursor()

    for rfid in rfid_list:
        cursor.execute("SELECT location FROM Residents WHERE barcode IN ('{0}');".format(rfid))
        location_result = cursor.fetchall()[0]
        postal_codes_list.append(location_result)
    cursor.close()
    # print(postal_codes_list)
    # get postal_codes_list base with rfid
    postal_codes_parsed = []
    for postal_code in postal_codes_list:
        postal_code_p = [int(s) for s in re.split('; |, |\*|\n|-|  | ', postal_code) if s.isdigit()][0]
        postal_codes_parsed.append(int(postal_code_p))

    postal_codes_parsed.sort(reverse=True)
    # print(postal_codes_parsed)
    return postal_codes_parsed


def ayuda_slot_assignment_algo(sorted_postal_code, qr_code_list):
    left_side = [1, 2, 3, 4, 5, 6]
    right_side = [7, 8, 9, 10, 11, 12]
    num_left = 0
    num_right = 0
    num = 0

    for postal_code in sorted_postal_code:
        num += 1
        for qr_code in qr_code_list:

            sqliteConnection = sqlite3.connect('barangay_residents.db')
            sqliteConnection.row_factory = lambda cursor, row: row[0]
            cursor = sqliteConnection.cursor()
            cursor.execute("SELECT location FROM Residents WHERE barcode IN ('{0}');".format(qr_code))
            location_result = cursor.fetchall()[0]
            qr_code_address = [int(s) for s in re.split('; |, |\*|\n|-|  | ', location_result) if s.isdigit()][0]

            cursor.execute("SELECT cabinet_num FROM Residents WHERE barcode IN ('{0}');".format(qr_code))
            check_assigned = cursor.fetchall()[0]

            if qr_code_address == postal_code and check_assigned == 0:
                # update this_qr_code cabinet#
                if (num % 2) == 0:
                    ayuda_slot_value = right_side[num_right]
                    num_right += 1
                    # if even

                else:
                    # if odd
                    ayuda_slot_value = left_side[num_left]
                    num_left += 1
                sql_update_query = """Update Residents set cabinet_num = {0}  where barcode = '{1}' """.format(ayuda_slot_value, qr_code)
                cursor.execute(sql_update_query)
                sqliteConnection.commit()
                cursor.close()
                break

                # update here qrcode cabinet number with ayuda_slot



    # for odd index assign to left_side then for even right_side
    # add update here

def clear_ayuda_cabinet_num():
    sqliteConnection = sqlite3.connect('barangay_residents.db')
    cursor = sqliteConnection.cursor()
    sql_update_query = """Update Residents set cabinet_num=0"""
    cursor.execute(sql_update_query)
    sqliteConnection.commit()
    cursor.close()

def get_info_cabinet_num(cabinet_num):

    sqliteConnection = sqlite3.connect('barangay_residents.db')
    # sqliteConnection.row_factory = lambda cursor, row: row[0]
    cursor = sqliteConnection.cursor()
    cursor.execute("SELECT location, contact, name, ayuda, barcode FROM Residents WHERE cabinet_num IN ('{0}');".format(cabinet_num))
    info_result = cursor.fetchall()
    location = info_result[0][0]
    postal_address = [int(s) for s in re.split('; |, |\*|\n|-|  | ', location) if s.isdigit()][0]
    contact = info_result[0][1]
    name = info_result[0][2]
    ayuda = info_result[0][3]
    barcode = info_result[0][4]
    #print(location, postal_address, contact, name, ayuda, barcode)
    return location, postal_address, contact, name, ayuda, barcode

clear_ayuda_cabinet_num()
#get_info_cabinet_num(1)