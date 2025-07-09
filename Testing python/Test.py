import os
os.system('cls')
students=[
("Alice", [85,90,88]),
("Bob", [70,75,80]),
("Charlie", [95,100,98])
]
# def add_student(name, scores):
#     for existing_name,_ in students:
#         if name.lower()==existing_name.lower():
#             print(f"{name} is already existed in the list.")
#             return 
#     student_scores=[]
#     for scores in scores.split(','): # This will let you enter scores separately by comma
#         student_scores.append(int(scores.strip())) #Add scores to the list and convert the scores variable to int
#     students.append((name,student_scores)) # add to parenthesis to make it become tuple or add two items
#     print(f"{name} added successfully.")
# def get_last_3_student():
#     return students[-3:]
# def update_score(name,index,new_score):
#     for i, (existing_name, existing_scores) in enumerate(students): # Enumerate use to get pair value 
#         if name.lower()==existing_name.lower():
#             if 0<=index<=len(existing_scores):
#                 existing_scores[index]=new_score # Update the score at the specified index
#                 students[index]=(existing_name,existing_scores) # Save the updated student record back to the list
#             print(f"{name}'s score has been updated.")
#             return
#         else:
#                 print("Invalid index")
#         return 
#     print(f"{name} not found.")
# def remove_student(name):
#     for i, (existing_name,_) in enumerate(students):
#         if name.lower()==existing_name.lower():
#             del students[i]
#             print(f"{name} removed from the list.")
#             return
#         print(f"{name} not found.")
 
def get_average(scores):
    return sum(scores) / len(scores)
    print(f"The average scores of the student is: {avg}")

# def get_all_average(students):
#     all_average=[]
#     for existing_name, existing_scores in students:
#         avg=get_average(existing_scores)
#         all_average.append((existing_name,avg))
#         return all_average
# def get_average(scores):
#     for existing_name, existing_score in students:
#         avg=get_average(existing_score)
#     print(f"The average scores of the student is: {avg}")
def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"
def grade_book(students):
    print(f"============================AUPP Gradebook Summary Report============================")
    print('-'*50)
    print(f"{'Name':<10}{'Average':<10}{'Grade':<10}")
    print('-'*50)
    for name,scores in students:
        avg=get_average(scores)
        grade=get_grade(avg)
        print(f"{name:<10}{avg:<10.2f}{grade:<10}")
    print("-" * 50)


if __name__ == "__main__":
    # student_name = input("Please enter a student name: ")
    # index=int(input("Enter number between 1-3:"))
    # student_scores = input("Enter the scores of the student separated by comma: ")
    # add_student(student_name, student_scores)
    # update_score(student_name,index,student_scores)
    # remove_student(student_name)
    # result=get_all_average(students)
    print(grade_book(students))
    result1=get_average()
    print(result1)
    print("\nCurrent student list:")
    for s in students:
        print(s)
    # print(get_last_3_student())
    

