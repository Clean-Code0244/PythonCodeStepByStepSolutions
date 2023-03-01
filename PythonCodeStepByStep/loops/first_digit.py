def first_digit(number):
    alfa = 0
    if(number < 0):
        number = -number
    gecici_number = number
    while(gecici_number > 0):
        alfa += 1
        gecici_number //= 10
    print(alfa)    
    last = 0
    for i in range(alfa):
        #if(number < 0):
            #number = -number
        last = number%10
        number //= 10
        
    
 
    return last








