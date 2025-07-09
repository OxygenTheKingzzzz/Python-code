import os
os.system('cls')
num=int(input("Enter your score:(0-100)"))
if num>=90 and num<=100:
    print("Grade A")
elif num>=80 and num<=89:
    print("Grade B")
elif num>=70 and num<=79:
    print("Grade C")
elif num>=60 and num<=69:
    print("Grade D") 
elif num>=50 and num<=59:
    print("Grade E")           
elif num<50:
    print("Grade F")
else:
    print("Invalid Number")