import os 
import math
os.system('cls')
x=float(input("Enter the first number:"))
y=float(input("Enter the second number:"))
print("---------------------------------------------------")
sum=x+y
differnce=x-y
product=x*y
quotient=x/y
power=pow(x,y)
sq=math.sqrt(x)
abso=abs(x-y)
print("Sum:",sum)
print("Differnce:",differnce)
print("Product:",product)
print("Quotient:",quotient)
print(f"{x} raised power of {y} is: {power}")
print(f"Square root of {x}: {sq}")
print(f"The absolute value of the difference between {x} and {y} is: {abso}")
    
    # Write a code about simple calculation using +,-,*,/,squareroot, and absolute value
    # This is chapter 2&3 lessons
#Hint: For squareroot include import math and use math.sqrt
    #  For absolute value we use abs bulit-in function
    # 