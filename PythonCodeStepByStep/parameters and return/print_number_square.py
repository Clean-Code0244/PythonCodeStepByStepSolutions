def print_number_square(a,b):
    
    liste = ""
    
    for i in range(a,b+1):
        liste += str(i)
    
    for i in range(0,len(liste)):
        if(i==0):
            print(liste[i:])
        elif(i<=10 and i>0):
            print(liste[i:],end="")
            print(liste[:i])
           
            








