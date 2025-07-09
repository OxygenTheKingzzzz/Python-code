'''
import os
os.system('cls')
# file_object=open('example.txt',mode='w',encoding='UTF-8') # Write if it doesnt has file or overwrite if existed file
# file_object=open('example.txt',mode='a',encoding='UTF-8') # append
file_object=open('example.txt',mode='r',encoding='UTF-8')
# file_object=open('example.txt','w')
# file_object.write('This is other example\n') #This line write "Hello World" to the file
result=file_object.read()
print(result)
'''

'''
file = open('notes.txt', 'w')
file.write("Hello, world!")
file.close()

file = open('notes.txt', 'r')
content = file.read()
print(content)
file.close()

try:
    myfile = open('example.txt', 'w')
    # myfile.write("Hello World")
    # perform operations
finally:
    myfile.close()
'''



# with open('example.txt', 'w') as file:
#     file.write("Hello, world!")
# with open('note.txt','w') as file_object:
#     file_object.write("This is an other example\n")
    
# with open('example.txt','r') as file:
#     content3=file.read(5)
#     content=file.readline()
#     content1=file.readline()
#     content2=file.readlines()
#     # content1=file_project.read(5)
#     # print(content1)
#     print(content)
#     print(content1)
#     print(content2)
#     print(content3)
    
    
# lines=["line 1\n","line 2\n", "line 3\n"]
# with open('mylist.txt','w') as file_project:
#     file_project.writelines(lines)
    
# mylist=[1,2,3]
# for i in mylist:
#     print(i, end=' ')
    
try:
    with open('myfile.txt', 'r') as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("The file 'myfile.txt' was not found. Please check the filename or create the file first.")