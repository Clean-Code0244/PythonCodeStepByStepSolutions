from random import randint
a  = int(input("Desired sum: "))
while True:
    b = randint(1,6)
    c = randint(1,6)
    sum = b+c
    print(b,"and",c,"=",sum)
    if sum == a:
        break








