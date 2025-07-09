import os
os.system('cls')
age=int(input("Enter ypur age:"))
if age<13:
    print("Child")
elif age>=13 and age<=19:
    print("Teenager")
elif age>=20 and age<=64:
    print("Adult")
else:
    print("Senior")
