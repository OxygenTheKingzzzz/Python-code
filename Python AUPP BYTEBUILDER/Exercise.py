import os
os.system('cls') #Input is the string datatype
# n1=int(input("Enter the value of number 1:"))
# n2=int(input("Enter the value of number 2:"))
# sum=n1+n2
# print("---------------------------------------")
# print(f"The result of {n1} + {n2} =",sum)
# print(f"The result of {n1} + {n2} = {sum}")
n1=int(input("Enter the value of number 1:"))
n2=int(input("Enter the value of number 2:"))
sum=n1+n2
deduct=n1-n2
multi=n1*n2
divide=n1/n2
oper=input("Enter the operator:")
print("---------------------------------------")
if oper == "+":
    print(f"The result of {n1} + {n2} =",sum)
elif oper =="-" :
    print(f"The result of {n1} - {n2} =",deduct)
elif oper =="*" :
    print(f"The result of {n1} * {n2} =",multi)
elif oper =="/" :
    print(f"The result of {n1} / {n2} =",divide)
else :
    print("Invalid operator")
    
