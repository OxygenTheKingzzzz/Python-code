#include<iostream>
#include<cmath>
using namespace std;
int main(){
    system("cls");
    double A,P,r,convert;
    int n,t;
    cout<<"Enter the principal amount:";
    cin>>P;
    cout<<"Enter the annual interest rate (in percentage):";
    cin>>r;
    cout<<"Enter the number of years:";
    cin>>t;
    cout<<"Enter the number of times interst is compounded per year:";
    cin>>n;
    convert=r/100;
    A=P*pow(1+convert/n,n*t);
    cout<<"The final amount after "<<t<<" years is: "<<A<<endl;
    return 0;
}