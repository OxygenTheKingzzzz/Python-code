#Practice 1
import os
os.system('cls')
n=int(input("Input a number:"))
d=dict()
for x in range(1,n+1):
    d[x]=x*x
print(d)
n=int(input("Input a number:"))
d={}
for x in range(1,n+1):
    d[x]=x*x
print(d)
# #Practice 2
# my_dict={'data1':100,'data2':-54,'data3':247}
# sum=0
# for i in my_dict:
#     sum+=my_dict[i]
# print(sum)

#Practice 3
'''
What if we want to know th keys that are associated with an item?
Can do this one at a time or build a complete reverse dictionary
'''
original={'A':1,'B':3,'C':3,'D':4,'E':1,'F':3}
#reverse={1:['A','E'],3:['C','B','F'],4:['D']}
def buildReverse(original):
    reverse={}
    for key,value in original.items():
        if value in reverse:
            reverse[value].append(key)
        else:
            reverse[value]=[key]
    return reverse
print(buildReverse(original))

#Filter a dictionary by conditions on keys or values
dictOfName={7:'sami',8:'jana',9:'rami',10:'rana',11:'reem',12:'salma'}
'''
Suppose we want to filter above dictionary by keeping only elements whose keys are even.
For that we can just iterate over all the items of dictionary and add elements with even key tp an another
dictionary
'''
newDict=dict()
for key,value in dictOfName.items():
    if key%2==0:
        newDict[key]=value
print(newDict)

#Filter a dictionary by keys in Python using dict comprehension
#Let's filter items in dictionary whose keys are even i.e. divisible by 2 using dict comprehension,
dictOfName={7:'sami',8:'jana',9:'rami',10:'rana',11:'reem',12:'salma'}
ND={key:value for (key,value) in dictOfName.items() if key%2==0}
print(newDict)

#Practice 4
#Write a Python program to drop empty Items from a given Dictionary.
dict1={'c1':'Red','c2':'Green','c3':None}
print("Original Dictionary")
print(dict1)
print("New Dictionary after dropping empty items:")
dict1={key:value for (key,value)in dict1.items() if value is not None}
print(dict1)

#Practice 5
#Write a python program to filter a dicionary based on marks greater than 70
marks={
    '1':75,
    '2':80,
    '3':65,
    '4':90
}
print("Original Dictionary:")
print(marks)
print("Marks greater than 70:")
result={key:value for (key,value) in marks.items() if value>70}
print(result)