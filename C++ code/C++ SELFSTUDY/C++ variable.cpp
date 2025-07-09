// #include<iostream>
// using namespace std;
// int main(){
// int x;
// int y=2025;
// int a,b;
// x=1;
// a=2,b=3;
// int 8std_name; error (start number)
// string StudentName; not recommend
// float break; error(keywords in C++)
// int std_id; correct
// string std_name; correct
// float std_match_score; correct 
// cout<<"x="<<x<<endl;
// cout<<"y="<<y<<endl;
// cout<<"a="<<a<<endl;
// cout<<"b="<<b<<endl;
// return 0;    
// }
// #include<iostream>
// #include<iomanip>
// using namespace std;
//sizeof
//datatype and variable
// int main(){
//     int id=1;
//     string name="Sasuke";
//     double salary=555.323;
//     float height=1.82;
//     char gender='M';
//     bool isActive=true;
//     cout<<"=================Athelete Information=================";
//     cout<<"ID:"<<id<<endl;
//     cout<<"NAME:"<<name<<endl;
//     cout<<"SALARY:"<<salary<<endl;
//     cout<<"HEIGHT:"<<height<<endl;
//     cout<<"GENDER:"<<gender<<endl;
//     cout<<"STATUS'S ACTIVATION:"<<isActive<<endl;
//     cout<<"========================================================";
// cout<<"size of short:"<<sizeof(short)<<endl;
// cout<<"size of long:"<<<sizeof(short)<<endl;
// cout<<"size of long:"<<sizeof(long)<<endl;
// cout<<"size of int:"<<sizeof(int)<<endl;
// cout<<"size of string:"<<sizeof(string)<<endl;
// cout<<"size of char:"<<sizeof(char)<<endl;
// cout<<"size of float:"<<sizeof(float)<<endl;
// cout<<"size of double:"<<sizeof(double)<<endl;
// cout<<"size of bool:"<<sizeof(bool)<<endl;
// return 0;
// }
#include<iostream>
#include<math.h>
using namespace std;
// Operation
int main(){
    int a=100,b=50;
    cout<<"Value of A:"<<a<<endl;
    cout<<"Value of B:"<<b<<endl;
    cout<<"Value of A+B:"<<a+b<<endl;
    cout<<"Value of A-B:"<<a-b<<endl;
    cout<<"Value of A*B:"<<a*b<<endl;
    cout<<"Value of A/B:"<<a/b<<endl;
    cout<<"Value of A%B:"<<a%b<<endl;
    cout<<"Value of (A+B)*2:"<<(a+b)*2<<endl;
    cout<<"Value of (A+B)*B:"<<(a+b)*b<<endl;
    cout<<"Value of POWER:"<<pow(2,3)<<endl;
    cout<<"Value of SQUARE ROOT:"<<sqrt(4)<<endl;
    cout<<"Value of (A^B)+A:"<<pow(a,b)+a<<endl;
    return 0;
}