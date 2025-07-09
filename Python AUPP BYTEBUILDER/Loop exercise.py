import os
os.system('cls')
chance= 4
while True:
    user_name="Oxygenzz"
    password=2211
    guessing_username=(input("Enter your username:"))
    if guessing_username == user_name:
        guessing_password=int(input("Enter your password:"))
        
        if guessing_password == password:
            print("Successfully Login!!")
            break
    elif guessing_username != user_name:
        print(f"Invalid username!!")
    elif guessing_password != password:
        print(f"Invalid password!! You have {chance} attempts left")
    elif chance==0:
        print("Access Denied")
chance -=1

