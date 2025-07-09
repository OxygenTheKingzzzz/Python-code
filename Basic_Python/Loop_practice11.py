import os
os.system('cls')
input_number=int(input("Insert a number: "))
total=0
while input_number>0:
    d=input_number%10
    total+=d
    input_number//=10
print(f"The answer of each digits sum up is: {total}")
