def window():
    # ZOR SORU
    str = "+"
    for j in range(2):
        for i in range(SIZE):
            str += "="
        str+="+"
    str1 = "|"
    for j in range(2):
        for i in range(SIZE):
            str1+=" "
        str1+="|"

    for j in range(3):
        print(str)
        if j == 2:
            break
        else:
            for i in range(SIZE):
                print(str1)













