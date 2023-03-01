def armstrong_numbers(num):
    if(num == 1):
        
        for j in range(0,10):
            
            if(isitPrime(j)):
                print(j,"",end="")
            
    elif(num <= 0):
        
        print("")
    else:
        
        for i in range(int(10**(num-1)),int(10**num)):
            
            if(isitPrime(i)):
                
                print(i,"",end="")

def isitPrime(number):
    a = str(number)
    c = number
    b = len(a)
    sum = 0
    while(c > 0):
        sum += (c % 10)**b
        c //= 10
    if(sum == number):
        return True
   
    return False
        
    


