import os
os.system('cls')
scores = {
 'Alice': 85,
 'Bob': 92,
 'Charlie': 78,
 'David': 90,
 'Eve': 88
}
sum=0
def print_highest_score():
    highest_key=None
    highest_value=float('-inf') # start with the smallest possible number
    for key,value in scores.items():
        if value >highest_value:
            highest_value=value
            highest_key=key
    return f"{highest_key} has the highest score: {highest_value}"
def average_score():
    global sum
    for score in scores.values():
        sum+=score
    avg=sum/len(scores)
    return avg
def new_grade():
    grade={}
    for key, value in scores.items():
        if value>=80:
            grade[key]=value
    return grade
print(average_score())
print(print_highest_score())
print(new_grade())