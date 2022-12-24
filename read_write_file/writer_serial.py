boolean_var = 0


def write_true():
    txt_file = open('testing.txt', 'r')
    state = int(txt_file.read())

    if state == 0:
        state = 1
    else:
        state = 0
    txt_file = open('testing.txt', 'w')
    txt_file.write(str(state))
    txt_file.close()
    print(state)


write_true()
