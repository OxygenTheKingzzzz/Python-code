#include<iostream>
#include<cmath>
using namespace std;
int main(){
    system("cls");
    // cout<<sqrt(64)<<endl;
    // cout<<round(4.6)<<endl;
    // cout<<min(1,10)<<endl;
    // cout<<max(1,10);
    double weight,height,BMI;
    cout<<"Input your weight:";
    cin>>weight;
    cout<<"Input your height:";
    cin>>height;
    // BMI=(weight/pow(height,2));
    BMI=(weight/(height*height));
    cout<<"Your BMI is:"<<BMI;
    return 0;
}