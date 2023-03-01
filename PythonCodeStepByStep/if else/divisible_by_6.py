number = int(input("Type a number: "))
if number % 2 == 0:
    if number % 3 == 0:
        print("Divisible by 6.")
else:
    print("Odd.")