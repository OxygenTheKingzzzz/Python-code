# import os
# os.system('cls')
# employee_details= {
#     101:'Ram',
#     102:'Shyam',
#     103:'Mohan',
#     "name":"Sak"
# }
# employee_details[101]='Sita'
# employee_details[104]='Gita'
# employee_details.update({105:'Dara'})
# del employee_details

# print(employee_details[101])
# print(employee_details)
# print(employee_details[104]) # Error
# print(employee_details.get(104,"404!! Error")) #Customize output
# print(employee_details.get(104)) #Return None 







# import os
# os.system('cls')
# my_list=[1,2,3,4,5,6,7,8,9,10]
# myData={
#     'name': 'John',
#     'age': 18
    
    
# }
# myList=["apple", "banana", "orange"]
# print(myList[0]) # You have to print the key value you cant do it like list
#Dictionaries are key-based not index-based.





# employee_details = {
#     201: 'Alice',
#     202: 'Bob',
#     203: 'Charlie'
# }

# # Task 1: Remove an employee using pop()
# employee_details.pop(202)
# # Example: removed_employee = employee_details.pop(202)

# # Task 2: Remove the last inserted item using popitem()
# employee_details.popitem()
# print(employee_details)
# # Example: last_item = employee_details.popitem()

# employee_details = {
#     101: 'Ram',
#     102: 'Shyam',
#     103: 'Mohan'
# }

# # Iterate over keys
# for key in employee_details:
#     print(key)

# # Iterate over values
# for value in employee_details.values():
#     print(value)

# # Iterate over key-value pairs
# for key, value in employee_details.items():
#     print(f"{key}: {value}")









import os
os.system('cls')
data = [{'email': 'ggabbitas0@weebly.com',
  'first_name': 'Gannie',
  'gender': 'M',
  'id': 1,
  'last_name': 'Gabbitas',
  'movie_gen': 'Comedy|Drama|Fantasy|Romance'},
 {'email': 'rpilling1@acquirethisname.com',
  'first_name': 'Richardo',
  'gender': 'M',
  'id': 2,
  'last_name': 'Pilling',
  'movie_gen': 'Action'},
 {'email': 'gporter2@sfgate.com',
  'first_name': 'Garret',
  'gender': 'M',
  'id': 3,
  'last_name': 'Porter',
  'movie_gen': 'Drama'},
 {'email': 'cspenton3@sfgate.com',
  'first_name': 'Cloe',
  'gender': 'F',
  'id': 4,
  'last_name': 'Spenton',
  'movie_gen': 'Action'},
 {'email': 'areally4@discovery.com',
  'first_name': 'Albertina',
  'gender': 'F',
  'id': 5,
  'last_name': 'Really',
  'movie_gen': 'Comedy|Drama|Romance'},
 {'email': 'pjuleff5@walmart.com',
  'first_name': 'Penny',
  'gender': 'M',
  'id': 6,
  'last_name': 'Juleff',
  'movie_gen': 'Comedy'},
 {'email': 'etetlow6@slate.com',
  'first_name': 'Eleanora',
  'gender': 'F',
  'id': 7,
  'last_name': 'Tetlow',
  'movie_gen': 'Children|Comedy'},
 {'email': 'gjellybrand7@psu.edu',
  'first_name': 'Gareth',
  'gender': 'M',
  'id': 8,
  'last_name': 'Jellybrand',
  'movie_gen': 'Comedy'},
 {'email': 'cabramowitz8@go.com',
  'first_name': 'Cathryn',
  'gender': 'F',
  'id': 9,
  'last_name': 'Abramowitz',
  'movie_gen': 'Drama'},
 {'email': 'kdavet9@discovery.com',
  'first_name': 'Konstantin',
  'gender': 'M',
  'id': 10,
  'last_name': 'Davet',
  'movie_gen': 'Action|Drama|Romance'},
 {'email': 'ssmidmorea@hexun.com',
  'first_name': 'Stillmann',
  'gender': 'M',
  'id': 11,
  'last_name': 'Smidmore',
  'movie_gen': 'Horror|Sci-Fi'},
 {'email': 'mmcilrathb@tamu.edu',
  'first_name': 'Matty',
  'gender': 'M',
  'id': 12,
  'last_name': 'McIlrath',
  'movie_gen': 'Thriller'},
 {'email': 'fspaduccic@about.com',
  'first_name': 'Fredric',
  'gender': 'M',
  'id': 13,
  'last_name': 'Spaducci',
  'movie_gen': 'Action|Horror'},
 {'email': 'acomberbachd@ifeng.com',
  'first_name': 'Anya',
  'gender': 'F',
  'id': 14,
  'last_name': 'Comberbach',
  'movie_gen': 'Comedy|Drama'},
 {'email': 'rpietzkere@globo.com',
  'first_name': 'Rubetta',
  'gender': 'F',
  'id': 15,
  'last_name': 'Pietzker',
  'movie_gen': 'Adventure|Animation|Children|Comedy'},
 {'email': 'tgeibelf@printfriendly.com',
  'first_name': 'Tiebold',
  'gender': 'M',
  'id': 16,
  'last_name': 'Geibel',
  'movie_gen': 'Drama|Film-Noir|Thriller'},
 {'email': 'ajenkinsg@netvibes.com',
  'first_name': 'Angus',
  'gender': 'M',
  'id': 17,
  'last_name': 'Jenkins',
  'movie_gen': 'Crime|Mystery'},
 {'email': 'cmoreinish@sogou.com',
  'first_name': 'Cassaundra',
  'gender': 'F',
  'id': 18,
  'last_name': 'Moreinis',
  'movie_gen': 'Documentary'},
 {'email': 'erainyi@dropbox.com',
  'first_name': 'Enrique',
  'gender': 'M',
  'id': 19,
  'last_name': 'Rainy',
  'movie_gen': 'Drama'},
 {'email': 'zbennetj@sogou.com',
  'first_name': 'Zollie',
  'gender': 'M',
  'id': 20,
  'last_name': 'Bennet',
  'movie_gen': 'Documentary'}]
# count_male=0
# count_female=0
# for data_item in data:
#     if data_item["gender"]=='M':
#         count_male+=1
#         print(data_item["gender"])    
# # for data_item in data:
#     elif data_item["gender"]=='F':
#         count_female+=1
#     # print(data_item("gender"))
#     print(data_item["gender"])
# print(count_male)
# print(count_female)
count_movie_gen=0
for data_item in data:
   if "Drama" in data_item['movie_gen']:
       count_movie_gen+=1
       print(data_item['movie_gen'])
print(count_movie_gen)





# university_data = {
#     "students": [
#         {
#             "id": "S001",
#             "name": "Alice",
#             "major": "Computer Science",
#             "courses": [
#                 {
#                     "code": "CS101",
#                     "name": "Intro to Programming",
#                     "grades": [85, 90, 88],
#                     "attendance": {
#                         "total": 30,
#                         "attended": 28
#                     }
#                 },
#                 {
#                     "code": "CS102",
#                     "name": "Data Structures",
#                     "grades": [80, 85, 82],
#                     "attendance": {
#                         "total": 30,
#                         "attended": 29
#                     }
#                 }
#             ]
#         },
#         {
#             "id": "S002",
#             "name": "Bob",
#             "major": "Information Systems",
#             "courses": [
#                 {
#                     "code": "IS201",
#                     "name": "Database Systems",
#                     "grades": [78, 82, 79],
#                     "attendance": {
#                         "total": 30,
#                         "attended": 25
#                     }
#                 },
#                 {
#                     "code": "CS101",
#                     "name": "Intro to Programming",
#                     "grades": [88, 87, 91],
#                     "attendance": {
#                         "total": 30,
#                         "attended": 30
#                     }
#                 }
#             ]
#         }
#     ],
#     "metadata": {
#         "semester": "Spring 2025",
#         "generated_on": "2025-06-16",
#         "admin": {
#             "name": "John Joe",
#             "email": "Joe@aupp.edu.kh"
#         }
#     }
# }
# print(university_data["students"][0]["courses"][0]["grades"])
# for data_items in university_data:
#   print(university_data["students"])