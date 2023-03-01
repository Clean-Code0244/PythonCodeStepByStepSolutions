from random import randint
def dice_sum():
    a = int(input("Desired dice sum: "))
    while True:
        b = randint(0,11)
        c = randint(0,11)
        print(b,"and",c,"=",(b+c))
        if((b+c) == a):
            break
        
            








