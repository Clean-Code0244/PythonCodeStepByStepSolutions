def main():
    total= 4 + 5 + 8 + 4
    # Calculate pay at work based on hours worked each day
    print("My total hours worked:")
    print(total)

    print("My hourly salary:")
    salary=8.75
    print(salary)

    print("My total pay:")
    pay = total * salary
    print(pay)

    print("My taxes owed:")  # 20% tax
    tax= 0.20
    taxes = pay * tax
    print(taxes)

main()