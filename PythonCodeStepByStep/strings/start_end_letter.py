def start_end_letter(string):
    count = 0
    newstring = string.lower()
    print("Looking for two \""+string+"\" words in a row.")
    while True:
        name = input("Type a word: ")
        if name[0].lower() == newstring and name[len(name)-1].lower() == newstring:
            count += 1
        else:
            count = 0
        if count == 2:
            print('"' + string + '"','is for','"'+ name + '"')
            break








