def plus_scores(text):
    file = open(text)
    read = file.read()
    myarray = read.split("\n")
    

    for i in range(0,len(myarray)-1,2):
        name = myarray[i]
        count = 0
        for j in myarray[i+1]:
            if j == "+":
                count += 1
        average = count / len(myarray[i+1]) * 100
        print(name + ": " + str(average) + "% plus")








