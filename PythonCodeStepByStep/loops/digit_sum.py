def digit_sum(integer):
    sum = 0
    alfa = str(integer)
    length = len(alfa)
    for i in range(length):
        if(integer < 0):
            integer = - integer
        sum += integer % 10
        integer //= 10
    return sum
    
        








