def factor_count(number):
    count = 0
    for i in range (1,number+1):
        if(number % i == 0):
            count += 1
    return count








