'''
import os
os.system('cls')
def square(number):
    return number**2
def sum(a,b):
    return 2*(a+b)  # Function that returns the sum of a and b
# This checks if the file is being run directly
if __name__=="__main__":
    # This part will only run if the script is executed directly
    print(sum(4,5))  
    print(square(60))
'''    


import os
os.system('cls')
def maxi(val1,val2,val3):
    max_value=val1
    if val2>max_value:
        max_value=val2
    if val3>max_value:
        max_value=val3
    return max_value
maxi(3,4,5)
if __name__=="__main__":
    print(maxi(3,4,5))
    