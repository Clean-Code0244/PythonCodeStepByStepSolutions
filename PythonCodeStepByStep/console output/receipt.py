def main():
    total = 38+40+30
    print("Subtotal:",total)
    
    # Compute total 
    
    tax = 0.08# owed, assuming
    totaltax = total*tax                 # 8% tax and
    print("Tax:",totaltax)
    tip = 0.15# 15% tip
    print("Tip:",total * tip)
    
    print("Total:",total + total * tax + total * tip)
    

main()