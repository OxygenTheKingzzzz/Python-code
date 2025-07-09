import os
os.system('cls')
count=0
for i in range(1,101):
    if(i%2==0):
        count+=1
        print(i)
        print(count)
for i in range(2,101,2):
    count+=1
print(count)