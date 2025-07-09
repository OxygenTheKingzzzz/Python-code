# int id;
#     string name,result;
#     char grade,gender;
#     float math,khmer,english,physics,avg,total_score;
#     cout<<"Enter student's ID:";
#     cin>>id;
#     cout<<"Enter student's name:";
#     cin>>name;
#     cout<<"Enter student's gender(M/F):";
#     cin>>gender;
#     cout<<"Enter Math score:";
#     cin>>math;
#     cout<<"Enter Khmer score:";
#     cin>>khmer;
#     cout<<"Enter English score:";
#     cin>>english;
#     cout<<"Enter Physics score:";
#     cin>>physics;
#     total_score=(math+khmer+english+physics);
#     avg=total_score/4;
#     if(avg>=90 &&avg<=100){
#         grade='A';
#     } 
#     else if(avg>=80 &&avg<=89.99){
#         grade='B';
#     }
#     else if(avg>=70 &&avg<=79.99){
#        grade='C';
#     }
#     else if(avg>=60 &&avg<=69.99){
#         grade='D';
#     }
#     else if(avg>=50 && avg<=59.99){
#         grade='E';
#     }
#     else if(avg>=0 &&avg<=49.99){
#         grade='F';
#     }
#     if(avg>=50){
#        result="PASS!!";
#     }
#     else{
#         result="FAIL!!";
#     }
#     cout<<"=======================STUDENT REPORT======================="<<endl;
#     cout<<"Student's ID:"<<id<<endl;
#     cout<<"Student's Name:"<<name<<endl;
#     cout<<"Student's Gender:"<<gender<<endl;
#     cout<<"Sudent's Math score:"<<math<<endl;
#     cout<<"Sudent's Khmer score:"<<khmer<<endl;
#     cout<<"Sudent's English score:"<<english<<endl;
#     cout<<"Sudent's Physics score:"<<physics<<endl;
#     cout<<"Student's Total score"<<total_score<<endl;
#     cout<<"Student's Average:"<<avg<<endl;
#     cout<<"Student's Grade:"<<grade<<endl;
#     cout<<"Student's Result:"<<result<<endl;
import os
os.system('cls')
id=int(input("Enter Student's ID:"))
name=input("Enter Student's Name:")
gender=input("Enter Student's Gender(M/F):")
math=float(input("Enter Student's Math Score:"))
khr=float(input("Enter Student's Khmer Score:"))
english=float(input("Enter Student's English Score:"))
physics=float(input("Enter Student's Physics Score:"))
total_score=math+khr+english+physics
avg=total_score/4
if avg >=90 and avg <=100:
    grade='A'
elif avg>=80 and avg<=89.99:
    grade='B'
elif avg>=70 and avg<=79.99:
    grade='C'
elif avg>=60 and avg<=69.99:
    grade='D'
elif avg>=50 and avg<=59.99:
    grade='E'
elif avg>=0 and avg<=49.99:
    grade='F'
if avg>=50:
    result="PASS!!"
else:
    result="FAIL!!"
print("=======================STUDENT REPORT=======================")
print(f"Student's ID: {id}")
print(f"Student's Name: {name}")
print(f"Student's Gender: {gender}")
print(f"Sudent's Math score: {math}")
print(f"Sudent's English score: {english}")
print(f"Sudent's Physics score: {physics}")
print(f"tudent's Total score: {total_score}")
print(f"Student's Average: {avg}")
print(f"Student's Grade: {grade}")
print(f"Student's Result: {result}")