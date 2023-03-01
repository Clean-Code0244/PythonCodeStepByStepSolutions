def to_morse_code(dictionary,string):
    new_str = ""
    for i in range(len(string)):
        if string[i].upper() in dictionary.keys():
            new_str+= dictionary[string[i].upper()]+" "
    print(new_str)







