def coin_flip(text):
    file = open(text)
    read = file.read()
    split = read.split()
    count = 0
    for i in split:
        if i.lower()=="h" or i.lower() == "heads":
             count += 1
    average = count / len(split) * 100
    if average >= 50:
        print(count,"heads "+"("+str(average)+"%)")
        print("You win!")
    else:
        print(count, "heads " + "(" + str(average) + "%)")
        print("You lose!")








