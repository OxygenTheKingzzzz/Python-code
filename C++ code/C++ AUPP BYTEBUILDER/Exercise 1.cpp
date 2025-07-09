// #include<iostream>
// using namespace std;
// int main(){
//     system("cls");
//     string name="Sak";
//     cout<<"What is your name?"<<endl;
//     cout<<"My name is "<<name;
//     return 0;
// }
// #include<iostream>
// using namespace std;
// int main(){
//     system("cls");
//     int age;
//     cout<<"Enter your age:";
//     cin>>age;
//     if(age>=18){
//         cout<<"Can drink!!";
//     }
//     else{
//         cout<<"Can not you are illegal!!";
//     }
//     return 0;
// }
#include<iostream>
#include<cmath>
using namespace std;
int main(){
    system("cls");
    /*Ber yg dak int pel tang variable hz lek jaek ot dach so we have to tang float or double instead*/
    double num1,num2;
    cout<<"Enter the first number:";
    cin>>num1;
    cout<<"Enter the second number:";
    cin>>num2;
    cout<<"Result:"<<endl;
    double sum=num1+num2;
    cout<<"Sum:"<<sum<<endl;
    double difference=num1-num2;
    cout<<"Differnce:"<<difference<<endl;
    double product=num1*num2;
    cout<<"Product:"<<product<<endl;
    double quotient=num1/num2;
    cout<<"Quotient:"<<quotient<<endl;
    cout<<num1<<" raised to power of "<<num2 <<" is :" <<pow(num1,num2)<<endl;
    cout<<"Square root of "<< num1 <<" is :"<< sqrt(num1)<<endl;
    cout<<"Absolute value of the difference between " << num1 << " and " << num2 << " is: " << fabs(num1-num2)<<endl;
    return 0;
}