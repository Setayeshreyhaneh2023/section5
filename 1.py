import random
n = int(input("the length of your list:"))
your_list=[]

for i in range(n):
    number = random.randint(0,500)
    if number not in your_list:
        your_list.append(number)
print (your_list)