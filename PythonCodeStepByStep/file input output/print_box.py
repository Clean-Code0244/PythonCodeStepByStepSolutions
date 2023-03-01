def print_box(text,number):
    file = open(text)

    split = file.readlines()
    new_array = []
    for i in split:
        if len(i) != 0:
            b = i[0].upper() + i[1:len(i)-1].lower()
            new_array.append(b)
    

    print("#"*number)
    for i in range(len(new_array)):
        if new_array[i] == "\n":
            print("#"+(number-2)*" "+"#")
        elif len(new_array[i]) <= number-2 :
            print("#"+new_array[i]+(number-2-len(new_array[i]))*" "+"#")

        else:
            print("#"+new_array[i][:number-2]+"#")
    print("#" * number)








