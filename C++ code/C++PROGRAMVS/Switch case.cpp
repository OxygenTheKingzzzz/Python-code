#include<iostream>
using namespace std;
int main(){
    // int s=5;
    // switch(s){
    // case 1:
    // cout<<"number one";
    // break;
    // case 2:
    // cout<<"number two";
    // break;
    // case 3:
    // cout<<"number three";
    // break;
    // default:
    // cout<<"Doesn't match the number";
    // }
    cout<<"****************All Product Type*******************"<<endl;
    cout<<"1.Grocery"<<endl;
    cout<<"2.Vegetable"<<endl;
    cout<<"3.Fruit"<<endl;
    cout<<"4.Meat"<<endl;
    cout<<"5.Exit"<<endl;
    cout<<"*******************Thank You***********************"<<endl;
    int num;
    cout<<"[+]Insert num"<<endl;
    cin>>num;
    switch(num){
        case 1:
        cout<<"1.Grocery"<<endl;
        break;
        case 2:
        cout<<"2.Vegetable"<<endl;
        break;
        case 3:
         cout<<"3.Fruit"<<endl;
         break;
         case 4:
         cout<<"4.Meat"<<endl;
         break;
         case 5:
         cout<<"5.Exit"<<endl;
         break;
         
    }

    return 0;
}