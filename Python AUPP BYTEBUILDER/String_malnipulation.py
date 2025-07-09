import os
os.system('cls')
name=" hello world "
"""
print(name.strip()) #Remove space both ends
print(name.lstrip()) #Remove space from the start only
print(name.rstrip()) #Remove space from the end only
print(name.upper()) #Convert all characters to uppercase
print(name.title()) #Capitalize the first letter of each word
print(name.lower()) #Capitalize the first letter of each word
print(name.capitalize()) #Capitalize only the first letter of the string
"""


"""
user_input=name.find("l") #Find the index of the first occurrence of "text" (returns -1 if not found)
user_replace=name.replace("l","x") #Replace all occurrences of "old" with "new"
print(user_input)
print(user_replace)

user_len=len(name)
user_len1=name.count("o")
print(user_len)
print(user_len1)
"""


# alp="ABC"
# digit=123
# user_method1=alp.isalpha()
# user_method2=digit.isdigit()
# print(user_method1)
# print(user_method2)



"""
# List of fruits
fruits = ["apple", "banana", "carrot"]

# Pick a random fruit from the list
Selected_fruit = fruits[0]   # Let's pick "apple"
#Fix the code to make it print correct even though user input is capitalize or mix lower and upper 
while True:
    ask_user = input("Guess the fruit: ").strip()    
    if ask_user.lower() == Selected_fruit:
        print("Correct! You guessed it right 🎉")
        break
    else:
        print("Wrong guess. Try again!")
"""



"""
sentence="I love python"
data="apple, banana, carrot"
paragraph="Python is fun, It is easy to learn. Let's code!"
#using split() will convert string into list
word2=paragraph.split(",")
words=sentence.split()
word1=data.split(",")
print(words)
print(word1)
print(word2)
"""


#using join will convert list into string
words=["I","love","python"]
joined="-".join(words)
print(joined)