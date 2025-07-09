#include<iostream> 
using namespace std;
int main(){ 
    // int num;
    // cout<<"[+]Insert number:";
    // cin>>num;


    // if(num>=0){
    //     cout<<"num is greater than 0";
    // }
    // if(num<=0){
    //     cout<<"answer";
    // }
    // if(num!=0 && num>0){
    //     cout<<"num is greater than 0";
    // }
    // if(num!=0 || num>0){
    //     cout<<"This is the answer of OR"<<endl;
    // }
    // if(num!=0 && num>0){
    //     cout<<"This is the answer of AND";
    // }
    // if(num==0){
    //     cout<<"number equal 0"<<endl;

    // }
    // else if(num<=0){
    //     cout<<"your answer"<<endl;}
    // else{
    //         cout<<"This is your answer";
    //     }
    double phy,che,bio,mat,khr,his,eng;
    cin>>phy;
    cin>>che;
    cin>>bio;
    cin>>mat;
    cin>>khr;
    cin>>his;
    cin>>eng;
    double total = phy+che+bio+mat+khr+his+eng;
    if(total<500 && total>427){
        cout<<"G=A"<<endl;
    }
        else if(total<426 && total>350){
            cout<<"G=B"<<endl;
        }
    else if(total<349 && total>300){
        cout<<"G=C"<<endl;
    }
    else if(total<299 && total>250){
    cout<<"G=D"<<endl;
    }
    else if(total<249 && total>200){
        cout<<"G=E"<<endl;
    }
    else {
        cout<<"G=F"<<endl;
    }

    return 0;
    
}