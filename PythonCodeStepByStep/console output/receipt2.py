def main():
    subtotal = int(input("What was the meal cost? $"))
    # Calculate total owed, assuming 8% tax / 15% tip
  
    tax = subtotal * .08
    tip = subtotal * .15
    total = subtotal + tax + tip
    
    print("Subtotal:", subtotal)
    print("Tax:", tax)
    print("Tip:", tip)
    print("Total:", total)

main()