import os
os.system('cls')
# def myFunctionTest():
#     print("Hello welcome to function calling")
# def myFunctionInputAndOutput():
#     id=int(input("Enter ID:"))
#     name=(input("Enter Name:"))
#     gender=(input("Enter Gender:"))  
#     print(f"ID: {id}")
#     print(f"Name: {name}")
#     print(f"Gender: {gender}")
# myFunctionTest()
# myFunctionInputAndOutput()
# def myFunctionInputAndOutput(id, name, gender):
#     print(f"ID: {id}")
#     print(f"Name: {name}")
#     print(f"Gender: {gender}")
# # myFunctionTest()
# myFunctionInputAndOutput(101, "John", "Male")
def sum():
    print(f"==============Find the sum of two value==============")
    a=int(input("Input a:"))
    b=int(input("Input b:"))
    total=a+b
    print(f"Sum of {a} + {b} = {total}")
def mul():
    print(f"==============Find the muliply of two value==============")
    x=int(input("Input x:"))
    y=int(input("Input y:"))
    total=x*y
    print(f"Result of {x} x {y} = {total}")
sum()
mul()