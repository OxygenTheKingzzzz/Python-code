# import os
# os.system('cls')
# try:
#     a=int(input("Enter number 1:"))
#     b=int(input("Enter number 2:"))
#     result=a/b
# except (ValueError, ZeroDivisionError) as e:
#     print("Oops! Something went wrong:", e)
# except Exception as e:
#     print("An unknown error occured.",e)
# else: 
#     print("The result is:", result)
import os
os.system('cls')
try:
    x=int(input("Enter a number: "))
    y=10/x
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception:
    print("An unknown error occured.")
else:
    print("Success! The result is: ",y)
finally:
    print("End of calculation!!") 