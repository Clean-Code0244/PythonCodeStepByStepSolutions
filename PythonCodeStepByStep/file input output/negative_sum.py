def negative_sum(text):
    file = open(text)
    read = file.read()
    split = read.split()
    
    sum = 0
    count = 0
    for i in split:
        sum += int(i)
        count += 1
        if sum < 0:
            print(sum,"after",count,"steps")
            return True

    print("no negative sum")
    return False








