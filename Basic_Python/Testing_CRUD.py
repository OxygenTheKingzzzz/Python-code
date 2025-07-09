import os
os.system('cls')
students=[
("Alice", [85,90,88]),
("Bob", [70,75,80]),
("Charlie", [95,100,98])
]
def add_student(name, scores):
    for existing_name,_ in students:
        if name.lower()==existing_name.lower():
            print(f"{name} is already existed in the list.")
            return 
    student_scores=[]
    for scores in scores.split(','): # This will let you enter scores separately by comma
        student_scores.append(int(scores.strip())) #Add scores to the list and convert the scores variable to int
    students.append((name,student_scores)) # add to parenthesis to make it become tuple or add two items
    print(f"{name} added successfully.")
def get_last_3_student():
    return students[-3:]
def update_score(name,index,new_score):
    for i, (existing_name, existing_scores) in enumerate(students): # Enumerate use to get pair value 
        if name.lower()==existing_name.lower():
            if 0<=index< len(existing_scores):
                existing_scores[index]=new_score # Update the score at the specified index
                students[i]=(existing_name,existing_scores) # Save the updated student record back to the list
                print(f"{name}'s score has been updated.")
            else:
                print("Invalid index") 
            return 
    print(f"{name} not found.")
def remove_student(name):
    for i, (existing_name,_) in enumerate(students):
        if name.lower()==existing_name.lower():
            del students[i]
            print(f"{name} removed from the list.")
            return
    print(f"{name} not found.")
def get_average(scores):
    return sum(scores) / len(scores)
def get_all_average(students):
    all_average=[]
    for existing_name, existing_scores in students:
        avg=get_average(existing_scores)
        all_average.append((existing_name,avg)) # Double parenthesis mean the code will display output as tuple
    return all_average
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
    print("-"*50)
if __name__=="__main__":
    while True:
        print("==================Welcome to AUPP Grade Manager==================")
        print("1. Add student")
        print("2. Print the last 3 students added to the list")
        print("3. Update student's score")
        print("4. Remove student")
        print("5. Show all students' average")
        print("6. Grade summary report")
        print("7. Exit")
        choice=int(input("Insert a number for the system to operate:"))
        match(choice):
            case 1:
                input_student=input("Enter the name of the student:")
                input_scores=input("Enter the student scores seperate by comma:")
                add_student(input_student,input_scores)
            case 2:
                print(get_last_3_student())
            case 3:
                update_name=input("Enter the name of the student you want to update:")
                update_index=int(input("Enter index between 0-2 for update the scores in the category:"))
                update_score_student=int(input("Input new scores for the student:"))
                update_score(update_name,update_index,update_score_student)
            case 4:
                remove_name=input("Enter the student's name you want to remove from the list:")
                remove_student(remove_name)
            case 5:
                result=get_all_average(students)
                print(result)
            case 6:
                (grade_book(students))
            case 7:
                print("Exiting the application...")
                break