import random
n=int(input("Enter number:"))
a= []
for i in range(n):
    z=(random.randint(1,100))
    if z not in a:
        a.append(z)
for i in range(len(my_list)):
    print(my_list[i], end="")