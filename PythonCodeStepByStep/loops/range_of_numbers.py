def range_of_numbers(number1,number2):
    if(number1 < number2):
        for i in range(number1,number2+1):
            print(i,end=" ")
    elif(number1 > number2):
        for i in range(number1,number2-1,-1):
            print(i,end=" ")
    else:
        print(number1)








