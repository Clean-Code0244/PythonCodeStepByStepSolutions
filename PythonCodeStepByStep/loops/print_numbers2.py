def print_numbers2():
    number = 1
    for i in range(5,0,-1):
        print("."*(5-number),end="")
        for j in range(6,i,-1):
            print(number,end="")
        number += 1
        print()









