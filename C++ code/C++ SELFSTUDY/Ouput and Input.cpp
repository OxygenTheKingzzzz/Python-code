// #include<iostream>
// using namespace std;
// int main(){
// int x,y,z;
// cout<<"Input value x:";
// cin>>x;
// cout<<"Input value y:";
// cin>>y;
// cout<<"Input value z:";
// cin>>z;
// cout<<"value of x:"<<x<<endl;
// cout<<"value of y:"<<y<<endl;
// cout<<"value of z:"<<z<<endl;
// cout<<"x+y+z:"<<x+y+z<<endl;
// cout<<"x-y-z:"<<x-y-z<<endl;
// cout<<"x*y*z:"<<x*y*z<<endl;
//     return 0;
// }
#include <iostream>
#include<iomanip>
using namespace std;
int main(){
    int id;
    string name;
    char gender;
    float average;
    cout<<"Input ID:";
    cin>>id;
    cout<<"Input name:";
    cin.ignore();
    getline(cin,name);
    cout<<"Input gender:";
    cin>>gender;
    cout<<"Input average:";
    cin>>average;
    cout<<"===============Student Result==============="<<endl;
    cout<<"ID:"<<id<<endl;
    cout<<"Name:"<<name<<endl;
    cout<<"Gender:"<<gender<<endl;
    cout<<"Average:"<<average<<endl;
    cout<<"STYLE 2:"<<endl;
    cout<<"Id\tName\tGender\tAverage"<<endl;
    cout<<id<<"\t"<<name<<"\t"<<gender<<"\t"<<average<<"\t"<<endl;
    cout<<"STYLE 3:"<<endl;
    cout<<setw(10)<<"ID";
    cout<<setw(20)<<"Name";
    cout<<setw(10)<<"Gender";
    cout<<setw(15)<<"Average"<<endl;
    cout<<setw(10)<<id;
    cout<<setw(20)<<name;
    cout<<setw(10)<<gender;
    cout<<setw(15)<<average;
    return 0;
}