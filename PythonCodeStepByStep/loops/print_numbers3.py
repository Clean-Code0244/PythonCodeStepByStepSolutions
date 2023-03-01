def print_numbers3():
    number = 0
    for i in range(1,6):
        for j in range(1,6):
            if(j == 5 - number):
                print(number+1,end="")
                number += 1
            else:
                print(".",end="")

        print()







