text = input("Input file? ")
file = open(text)
read = file.read()
split = read.split()

numbers = ["0","1","2","3","4","5","6","7","8","9","-"]
new_array = []
for i in split:
    for j in numbers:
        if i.startswith(j):
            new_array.append(i)


for i in range(len(new_array)-1):

    a = float(new_array[i+1])-float(new_array[i])
    b = int(a*100)/100
    print(new_array[i],"to",new_array[i+1]+", change =",round(b,1))







