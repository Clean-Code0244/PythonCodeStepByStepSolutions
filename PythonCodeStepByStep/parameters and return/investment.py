def amount(initial_amount,interest_rate,month):
    Future_Value = initial_amount * ( 1 + interest_rate )**month
    return Future_Value
def Profit(initial_amount,a):
    return a-initial_amount
def percentage(initial_amount,a):
    return round((a-initial_amount)/initial_amount * 100)

def main():
    for i in range(1,3):
        print("Investor",i)
        initial_amount = float(input("Initial amount? "))
        interest_rate = float(input("Interest rate%? "))
        month = int(input("Num. of months? "))
        a = amount(initial_amount,interest_rate,month)
        print("Amount: $",round(a,2))
        profit = Profit(initial_amount,a)
        percentage1 = percentage(initial_amount,a)
        print("Profit: $",round(profit,2),"=",percentage1,"%")
        if percentage1>=0 and percentage1<=10:
            print("Weak")
        elif percentage1>10 and percentage1<=50:
            print("Medium")
        else:
            print("Strong")
        print()
    print("Have a nice day!")

main()








