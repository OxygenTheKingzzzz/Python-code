import os
os.system('cls')
# dic={
#     'Name':'Zara',
#     'Age':7,
#     'Class':'First'
# }
# print(dic)

# dict={}
# dict['Name']='Zara'
# dict['Age']=7
# dict['Class']='First'
# print(dict)
# print(dict['Age'])

# dict={
#     'Name':'Zara',
#     'Age':7,
#     'Class':'First',
#     'Class':'Last'
# } #When there are duplicate values it will overwrite existing values.
# print(dict)

# dict={
#     'Name':'Zara',
#     'Age':7,
#     'Class':'First'
# } #Len in dictionary will count number of items in the dictionary
# print(len(dict))
# # The value in dictionarry items can be of any data type:
# # Example: String,int,boolean, and list data types
# thisdict={
#     'brand':'Ford',
#     'eletric':False,
#     'year':1964,
#     'colors':['red','white','blue']
# }
# print(thisdict)

# # You can access the items of a dictionary by referring to its key name, inside sqare brackets
# # Thre is also a method called get() that will give you the same result:
# #Example: Get the value of the "Class" key:
# x=dict.get("Class")
# print(x)

car={
    'brand':'Ford',
    'model':'Mustang',
    'year':1964
}
# x=car.keys() 
# print(x) #This will print all keys in dict
# car['color']='white' 
# print(x) #Add a new itme to the original dict, after change and print you will see it updated as well

# #The items() method will return each item in a dictionary, as tuples in a list\
# y=car.items()
# print(y)
# #Check if Key Exists
# #To determine if a specified key is present in a dictionary use the in keyword:
# #Check if "Model" is present in the dictionary
# if "model" in car:
#     print("Yes, 'model' is one of the keys in the car dictionary")
# #change values 
# car['year']=2018
#this will change the value of the key 'year'
#Update dictionary
'''
The update() method will update the dictionaryu with the items from the given argument.
THe argument must be a dictionary, or an iterable object with key:value pairs
'''
#Example: Update the 'year' of the car by using the update() method
# car.update({'year':2020})
# print(car)
# #Adding an item to the dict is done by using a new index key and assigning a value to it:
# car['color']='red'
# print(car)
# '''
# For update() method if the item does not exist, the item will be added.
# '''
# #Example: Add a color item to the dictionary by using the update() method
# car.update({'owner name':'me'})
# print(car)
# '''
# There are several methods to remove items from a dictionary
# '''
# car.pop('model')
# print(car)
# #The car popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead)
# car.popitem()
# print(car)
# # The del keyword removes the item with the specified key name:
# del car['brand']
# print(car)
# #del can be use to delete the whole dict as well
# del car
# print(car) # this will cause error because 'car' no longer exist
#The clear() method empties the dictionary (It clears everything in the dict)
# car.clear()
# print(car)
'''
You can loop through a dictionary by using a for loop.
When looping through a dictionary, the return value are the keys of the dictionary, 
but there are methods to return the values as well.
'''
for x in car:
    print(x) # This will only print all keys in the dictionary
for x in car:
    print(car[x]) #This will print all values in the dictionary


# You can also use the values() method to return values of a dictionary:
for x in car.values():
    print(x)

#You can use the keys() method to return the keys of a dictionary:
for y in car.keys():
    print(y)
#Loop through both keys and values, by using the items() method:
for a,b in car.items():
    print(a,b)

#Display a dicitioonary in sorted order on keys
dict={
    'Name':'Zara',
    'Age':7,
    'Class':'First',
    'Grade':70
}
for x in sorted(dict):
    print(x,dict[x])


