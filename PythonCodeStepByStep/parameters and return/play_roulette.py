from random import randint
def play_roulette(money,bet):
    #start with $ 10 and bet up to $ 3
    print("start with $", money, "and bet up to $", bet)
    print("bet\tspin\tmoney")
    temp_bet = bet
    list = []
    while True:
        if money<=temp_bet:
            bet = money
        else:
            bet = temp_bet
        spin = randint(0,36)
        if spin == 0:
            money -= bet
        elif spin % 2==0:
            money += bet
        else:
            money -= bet



        print(str(bet) + "\t" + str(spin) + "\t" + str(money))
        list.append(money)
        if money<=0:
            a = max(list)
            print("max money: $",a)
            break

def max(list):
    max = list[0]
    for i in list:
        if i>=max:
            max = i
    return max




