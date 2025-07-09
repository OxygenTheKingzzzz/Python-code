import os
os.system('cls')
pw="Iamatomic"
while True:
    guess_pw=input("Enter your pw:")
    if guess_pw==pw:
        print("Correct password!!")
        break
    else:
        print("You are incorrect!!")
    