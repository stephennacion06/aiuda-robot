prev_value = 0
while True:
    txt_file = open('testing.txt', 'r')
    try:
        value = int(txt_file.read())
        prev_value = value
    except:
        value = prev_value
    print(value)
