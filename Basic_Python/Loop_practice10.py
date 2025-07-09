import os
os.system('cls')
print("======================Welcome to AUPP Grocery Store======================")
grocery_name=[]
grocery_price=[]
while True:
    name_input=input("Enter the product name:")
    price_input=float(input("Enter the price of the product:"))
    grocery_name.append(name_input)
    grocery_price.append(price_input)
    total=sum(grocery_price)
    ask_user=input("Do you want to add more product (Y/N):")
    if ask_user.upper()=='N':
        break
print(f"Name of the products:{grocery_name}")
print(f"Price of the product: {grocery_price}")
print(f"Total cost: {total}")