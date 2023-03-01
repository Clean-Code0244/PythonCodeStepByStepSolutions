b = 0
sum = 0
while True:
    a = int(input("Integer? "))
    if(a == 0):
        break
    elif(a % 2 == 0):
        sum += a
        b += 1
    
average =  sum / b
print("Average:",average)