from random import randint
def  random_walk():
    position = 0
    maximum = 0
    print("position =",position)
    while True:
        if(position == 3):
            
            print("max position =",maximum)
            break
        elif(position == -3 ):
            
            print("max position =",maximum)
            break
            
            
        k = 0
        a = randint(1,10)
        if(a % 2 == 0):
            k = 1
            position += k
            print("position =",position)
            if(position >= maximum):
                maximum = position
            
        else:
            k = -1
            position += k
            print("position =",position)
            if(position >= maximum):
                maximum = position
    
    








