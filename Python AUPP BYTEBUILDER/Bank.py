import os
os.system('cls')
P=float(input("Enter the principal amount:"))
r=float(input("Enter the annual interest rate(in percentage):"))
t=float(input("Enter the year:"))
n=float(input("Enter the number of times interest is compounded per year:"))
convert= r/100
A=P*pow(1+convert/n,n*t)
a=round(A,2)
print(f"The final amount after {t} year is: {a}")

#Write a code about the interest formula
#Hint: It is similar to other formula exercises  
#It is in chapter 2&3 
# compound interest formula= A=P*(1=r/n)^(n*t)
#A is final amount
#P is the principal amount 
#r is the anuual interest rate(as decimal)
#n is the number of times interest is compounded per year
#t is the number of years
#convert r to decimal= r/100
#hint = use pow