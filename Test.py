def num():
    max_number = {}
    num = 10
    x = 0
    while 0 < num:
        max_number[x] = x
        x += 1
        num -= 1
    print(max_number)


num()
