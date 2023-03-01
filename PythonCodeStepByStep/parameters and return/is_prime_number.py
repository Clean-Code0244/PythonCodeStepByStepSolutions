def is_prime_number(number):
    if(number == 2):
        return True
    elif(number <= 1):
        return False
    for i in range(2,number):
        if(number % i == 0):
            return False
    return True
    








