import random
def coin_flip(request,c_face):
    if(c_face=='H'):
        cc=0
    elif(c_face=='T'):
        cc=1
    else:
        print("ERROR!")
        return
        
    if(request==0):
        print("You got "+c_face+" "+str(request)+" times in a row!")
        return
    elif(request<0):
        print("ERROR!")
        return

    count=0
    while(count<=request):
        coin=random.choice('HT')
        if(c_face==coin):
            count+=1
        else:
            count=0
        print(coin,end=" ")
    print("\nYou got "+c_face+" "+str(request)+" times in a row!")