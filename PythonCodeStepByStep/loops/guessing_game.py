from random import randint
def total(liste):
    sum = 0
    for i in liste:
        sum += i
    return sum

def main3(liste):
    min = liste[0]
    for i in liste:
        if i<= min:
            min = i
    return min
def main2():
    temp_list = []
    str = "I'm thinking of a number between 1 and 100..."
    number = randint(1, 100)
    count = 0

    temp_list.append(str)
    temp_list.append(number)
    temp_list.append(count)
    return temp_list

def main():
    print("This program allows you to guess random numbers.")
    print("I will think of a number between 1 and 100")
    print("and you will try to guess it.")
    print("After each guess, I will give you a clue about")
    print("whether the correct number is higher or lower.")


    liste = main2()
    number = liste[1]
    str = liste[0]
    count = liste[2]
    counter_list = []
    total_game = 1
    print()
    print(str)
    while True:
        count += 1
        guess = int(input("Your guess? "))
        if number < guess:
            print("It's lower.")


        elif number > guess:
            print("It's higher.")


        else:
            if count == 1:
                print("You got it right in", count, "guess!")
            else:
                print("You got it right in", count, "guesses!")
            counter_list.append(count)
            replay = input("Do you want to play again? ")
            if replay.lower().startswith("y"):
                new_list = main2()
                number = new_list[1]
                str = new_list[0]
                count = new_list[2]
                total_game += 1
                print()
                print(str)
            else:
                print()
                print("Overall results:")
                a = total_game
                print("Total games   =",a)
                b = total(counter_list)
                print("Total guesses =",b)
                print("Guesses/game  =",round((b/a),1))
                c = main3(counter_list)
                print("Best game     =",c)
                break
main()

