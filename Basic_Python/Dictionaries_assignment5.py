"""
5. Build a simple console-based student management system that uses Python dictionaries to store
and manage data about students, their courses, and grades.
Store student data in a dictionary, where:
• Each key is a student ID (or name).
• Each value is another dictionary containing:
o 'name': full name
o 'courses': a dictionary of courses and grades.
Example structure:
students = {
 'S001': {
 'name': 'Alice',
 'courses': {'Math': 90, 'English': 85}
 },
 'S002': {
 'name': 'Bob',
 'courses': {'Math': 75, 'Science': 80}
 }
}
• Feature to implement
1. Add a new student.
2. Add or update a course & grade for a student.
3. Remove a student by ID.
4. Display all students with their courses and grades.
5. Display the average grade for a given student.
6. Find the student(s) with the highest average grade.
"""
import os
os.system('cls')
student_data={}
def add_student(student_id,student_name,courses):   
    if student_id in student_data:
        print("This ID already existed with a student's name!!")
        return
    # Declare that the key of the first dict will hold the value of another dict
    student_data[student_id]={
        'name':student_name,
        'courses':courses
    }
    print(f"Student '{student_name}' added successfully.")
    
def add_update_course(student_id,course_name,score):
    if student_id not in student_data:
        print("Student not found.")
    else:
        """
        student_data → your main dictionary.
        student_data[student_id] → gets the info of one student.
        student_data[student_id]['courses'] → gets the inner dictionary of their courses and scores.
        .update({...}) → you are telling Python: “Hey, update this dictionary with another dictionary.”
        {course_name: score}
        is just a new small dictionary (like {"Math": 90}) that you're adding (or updating) inside 
        the existing courses dictionary.
        """
        student_data[student_id]['courses'].update({course_name:score})
        # student_data[student_id]['courses'][course_name] = score (This one is another way to add/update courses.)
        print(f"Course '{course_name}' updated/added for student.")
        
def delete_student(student_id):
    if student_id in student_data:
        del student_data[student_id]
        print(f"Student with ID: {student_id} deleted sucessfully.")
    else:
        print("Student not found!!")
        
def display_course_grade():
    if not student_data:
        print("There is no data in the management system.")
    for student_id,student_detail in student_data.items():
        print(f"ID:{student_id} \t Name:{student_detail['name']}")
        for course,score in student_detail['courses'].items():
            print(f"- {course}: {score}")

def display_average_grade(student_id):    
    if student_id not in student_data:
        print("There is no data in the management system.")
    course_data=student_data[student_id]['courses']
    if not course_data:
        print(f"Student '{student_data[student_id]['name']}' has no courses.")
        return
    avg=sum(course_data.values())/len(course_data.values())
    print(f"Average grade for '{student_data[student_id]['name']}' is {avg:.2f}")   

def display_highest_average():
    if not student_data:
        print("There is no data in the management system.")
    average={}
    for student_id,student_info in student_data.items():
        course=student_info['courses']   
        if course:
            average[student_id]=sum(course.values())/len(course.values())
        else:
            average[student_id]=0
    max_avg=max(average.values())
    best_students = [student_data[student_id]['name'] for student_id, avg in average.items() if avg == max_avg]
    """
    The code above is the shortcut of this one:
    best_students = []
    for student_id, avg in average.items():
    if avg == max_avg:
        best_students.append(student_data[sid]['name'])
    """
    for name in best_students:
        print(f"Highest average grade is {max_avg:.2f}, achieved by:{name}")
if __name__=="__main__":
    while True:
        print("===================Welcome to AUPP Student Management System===================")
        print("1. Add a new student")
        print("2. Add or update a course & grade for a student")
        print("3. Remove a student by ID")
        print("4. Display all students with their courses and grades")
        print("5. Display the average grade for a given student")
        print("6. Find the student(s) with the highest average grade")
        print("7. Exit") 
        choice=int(input("Enter a number for the system to operate(1-7):"))
        match(choice):
            case 1:
                student_id=input("Enter the student ID:")
                student_name=input("Enter the student name:")
                num_course=2
                courses={}
                for i in range(num_course):        
                    course=input(f"Enter the course{i+1} name:")
                    grade=int(input(f"Enter course{i+1} score:"))
                    courses[course]=grade
                add_student(student_id,student_name,courses)
            case 2:
                student_id=input("Enter the student ID:")
                course_name=input("Enter the course name:")
                score=int(input("Enter the score of the course:"))
                add_update_course(student_id,course_name,score)
            case 3:
                student_id=input("Enter the student ID:")
                delete_student(student_id)
            case 4:
                display_course_grade()
            case 5:
                student_id=input("Enter the student ID:")
                display_average_grade(student_id)
            case 6:
                display_highest_average()
            case 7:
                print("Exit application...")
                break
            case _:
                print("Invalid choice. Please select a number from 1 to 7.")