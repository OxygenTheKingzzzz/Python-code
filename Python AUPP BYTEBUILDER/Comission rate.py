# import os
# os.system('cls')
# # sale_amount=float(input("Please enter your sales amount:"))
# print(f"Sale Amount: \tComission:")
# for sale_amount in range (10000,100001,5000):
#     if sale_amount>=0.01 and sale_amount<=5000 :
#      comission=sale_amount*(0.06)
#     elif sale_amount>=5000.01 and sale_amount<=10000 :
#      comission=sale_amount*(0.08)
#     elif sale_amount>=10000.01 :
#      comission=sale_amount*(0.10)
#     # print(f"The comission rate of {sale_amount} is {comission}")

#     print(f"{sale_amount} \t\t{comission}")import os
# import os
# os.system('cls')  
# def get_commission(sale_amount):
#     if 0.01 >= sale_amount <= 5000:
#         return sale_amount * 0.06
#     elif 5000.01 >= sale_amount <= 10000:
#         return sale_amount * 0.08
#     elif sale_amount >= 10000.01:
#         return sale_amount * 0.10
#     else:
#         return 0.0  
# print("Sale Amount:\tCommission:")
# for sale_amount in range(10000, 100001, 5000):
#     commission = get_commission(sale_amount)
#     print(f"{sale_amount}\t\t{commission:.2f}")
# import os
# os.system('cls')  # Clear screen (Windows only)

# # Function to display commission table
# def show_commissions():
#     print("Sale Amount:\tCommission:")
#     for sale_amount in range(10000, 100001, 5000):
#         if 0.01 >= sale_amount <= 5000:
#             commission = sale_amount * 0.06
#         elif 5000.01 <= sale_amount <= 10000:
#             commission = sale_amount * 0.08
#         elif sale_amount >= 10000.01:
#             commission = sale_amount * 0.10
#         else:
#             commission = 0.0
#         print(f"{sale_amount}\t\t{commission:.2f}")

# # Call the function
# show_commissions()
import os 
os.system('cls')
sale_amount