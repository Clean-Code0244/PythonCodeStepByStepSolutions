def convert_to_alt_caps(string):
    string_array = []
    for i in range(len(string)):
        string_array.append(string[i])
    a = 0
    for i in range(len(string_array)):
        if string_array[i] == " ":
            a -= 1
        if a % 2 == 0:
            string_array[i] = string_array[i].lower()

        else:
            string_array[i] = string_array[i].upper()
        a += 1
    newstr = ""
    for i in string_array:
        newstr += i
    return newstr








