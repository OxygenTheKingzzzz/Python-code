import os
os.system('cls')
def subjects():
    math=float(input("Enter your math score:"))
    physic=float(input("Enter your physic score:"))
    bio=float(input("Enter your bio score:"))
    geo=float(input("Enter your geo score:"))
    chemistry=float(input("Enter your chemistry score:"))
    total=math+physic+bio+geo+chemistry
    average=total/5
    return average
    avg=average
def grades(average):
    if average>=90 and average<=100:
        return 'A'
    if average>=80 and average<=89:
        return 'B'
    if average>=70 and average<=79:
        return 'C'
    if average>=60 and average<=69:
        return 'D'
    if average>=50 and average<=59:
        return 'E'
    else:
        return 'F'
if __name__=="__main__":
# Calls the subjects() function
# Prompts the user to input 5 subject scores
# Calculates the average of all scores
# Stores the result in the variable avg
    avg = subjects()
# Calls the grades() function
# Passes the average score (avg) as an argument
# Checks which grade range it falls into (A, B, C, etc.)
# Stores the result in the variable grade
    grade = grades(avg)
    print(f"The average scores is: {avg}")
    print(f"The grade is: {grade}")
    