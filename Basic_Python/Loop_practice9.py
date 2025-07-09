import os
os.system('cls')
num=int(input("Enter any number you want to calculate its factorial:"))
d=1
i=1
while i<=num:
    d=d*i
    i+=1
print(f"The answer of {num} factorial={d}")
