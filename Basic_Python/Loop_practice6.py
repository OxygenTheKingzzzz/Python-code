import os
os.system('cls')
names=[]
while True:
    guess_name=input("Enter a name:")
    names.append(guess_name)
    if(guess_name=="done"):
        break
print(names)
    