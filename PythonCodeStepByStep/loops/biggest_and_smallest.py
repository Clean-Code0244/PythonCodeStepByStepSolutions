a = int(input("How many numbers? "))

liste = []
for i in range(a):
    b = int(input("Next number? "))
    liste.append(b)
max = liste[0]
min = liste[0]
for i in liste:
    if(i >= max):
        max = i
    elif(i <= min):
        min = i
print("Biggest =" , max)
print("Smallest =" , min)








