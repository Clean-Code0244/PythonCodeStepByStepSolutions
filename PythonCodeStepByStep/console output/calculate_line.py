print("This program calculates y coordinates for a line.")
m = int(input("Enter slope (m): "))
b = int(input("Enter intercept (b): "))

while True:
    x = int(input("Enter x: "))
    if(x == -1):
        break
    result = m*x + b
    print("f("+str(x)+") =",result)