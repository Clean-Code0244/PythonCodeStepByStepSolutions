s = input("What is your name? ")
s1 = s.find(" ")
text1 = "" 
text2 = ""
for i in range(s1):
    text1 += s[i]
for j in range(s1+1,len(s)):
    text2 += s[j]
    
print(text1+",",text1+",","bo-B"+text1[1:])
print("Banana-fana fo-F"+text1[1:])
print("Fee-fi-mo-M"+text1[1:])
print(text1.upper()+"!")
print()
print(text2+",",text2+",","bo-B"+text2[1:])
print("Banana-fana fo-F"+text2[1:])
print("Fee-fi-mo-M"+text2[1:])
print(text2.upper()+"!")

    








