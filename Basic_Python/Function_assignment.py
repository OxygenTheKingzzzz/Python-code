# import os
# os.system('cls')
# text=input("Please input a sentence:")
# def to_lower(text):
#     return text.lower()
# def to_upper(text):
#     return text.upper()
# def to_title(text):
#     return text.title()
# if __name__=="__main__":
#     print(f"lower sentence case: {to_lower(text)}")
#     print(f"upper sentence case: {to_upper(text)}")
#     print(f"title sentence case: {to_title(text)}")
    

import os
os.system('cls')
def to_lower(text):
    return text.lower()
def to_upper(text):
    return text.upper()
def to_title(text):
    return text.title()
if __name__=="__main__":
    text=input("Please input a sentence:")
    print(f"lower sentence case: {to_lower(text)}")
    print(f"upper sentence case: {to_upper(text)}")
    print(f"title sentence case: {to_title(text)}")
    


















    
'''    
def get_text():
    return input("Please input a sentence: ")
def to_upper(text):
    return text.upper()
def to_lower(text):
    return text.lower()
def to_title(text):
    return text.title()
if __name__ == "__main__":
    user_text = get_text()             # Get input from user
    print(to_upper(user_text))         # Pass it to another function
    print(to_lower(user_text))         # Same here
    print(to_title(user_text))
'''















'''
#Looping 
import os
os.system('cls')
def to_lower(text):
    return text.lower()
def to_upper(text):
    return text.upper()
def to_title(text):
    return text.title()
if __name__ == "__main__":
    while True:
        text = input("Please input a sentence (or type 'exit' to quit): ")
        if text.lower() == 'exit':
            print("Goodbye!")
            break
        print(f"lower sentence case: {to_lower(text)}")
        print(f"upper sentence case: {to_upper(text)}")
        print(f"title sentence case: {to_title(text)}")
        print()
'''