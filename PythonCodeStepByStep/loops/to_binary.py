def to_binary(number):
    normal = number
    
    if (number == 0):
        text = "0"
    else:
        text = ""
    text2 =""
    while(normal > 0):
        
        text += str(normal%2)
        normal //= 2
    for a in range(len(text)-1,-1,-1):
        text2 += text[a]
    return text2
        
        
            
        








