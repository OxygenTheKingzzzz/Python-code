"""
4. You are given a list of names:
names = ["Anna", "Benjamin", "Cathy", "Dann", "Eleanor", "Frank"]
Write a program to create a dictionary where the keys are name lengths and the values are lists of
names of that length:
Expected Output
{ 
 4: ['Anna', 'Dann'],
 7: ['Benjamin'],
 5: ['Cathy', 'Frank'],
 7: ['Eleanor']
}
"""
import os
os.system('cls')
names = ["Anna", "Benjamin", "Cathy", "Dann", "Eleanor", "Frank"]
new_name_dict={}
for name in names:
    length_name=len(name)
    if length_name not in new_name_dict:
# The line below is like after create a library, let us add a new shelf labeled with the number length, 
# and put the first book (name) on it.”
        new_name_dict[length_name]=[name] 
    else:
        new_name_dict[length_name].append(name)

print(new_name_dict)