def input_stats(text):
    file = open(text)
    read = file.read()
    split = read.split("\n")
    sum = 0
    longest = 0
    count = 0
    for  i in range(len(split)-1):
        sum1 = 0
        if longest <= len(split[i]):
            longest = len(split[i])

        count += 1
        sum += len(split[i])
        sum1  += len(split[i])

        print("Line",count,"has",sum1,"chars")
    
    print(count,"lines; longest = "+str(longest)+",","average =",sum/count)


