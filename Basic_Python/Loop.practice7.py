import os
os.system('cls')
# number=[]
count=5
total=0
while True:
    insert_num=int(input("Enter any number you want to sum:"))
    # number.append(insert_num)
    total+=insert_num
    count-=1
    print(f"You have {count} attempt left")
    if(count==0):
        print("Completed!")
        break
print(total)
