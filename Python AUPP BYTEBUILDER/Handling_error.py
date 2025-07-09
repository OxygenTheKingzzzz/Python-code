import os
os.system('cls')
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")
# if operator !='+' or '-' or '*' or '/':
#     print("Invalid operator! Please use one of: +, -, *, /")
#     result=0
# else:
#     result = None
try:
    match operator:
        case "+":
            result = num1 + num2
        case "-":
            result = num1 - num2
        case "*":
            result = num1 * num2
        case "/":
        # if num2 == 0:
        #         print("Error: Division by zero is not allowed.")
        #         result =0
        # else:
             result = num1 / num2
           
    print(f"The result of: {num1} {operator} {num2} = {result}")
except:
    pass

