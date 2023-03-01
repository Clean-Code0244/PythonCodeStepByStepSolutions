from random import randint
print("Welcome to Piglet!")
sum = 0
while True:
    a = randint(1,10)
    if(a == 1):
        print("You rolled a 1")
        sum = 0
        print("You got",sum,"points.")
        break
    else:
        
        print("You rolled a",a)
        sum += a
        b = input("Roll again? ")
        if(b == "no" or b == "n"):
            print("You got",sum,"points.")
            break
            
        
            
         
        
    








