#include<iostream>
using namespace std;
int main(){
    system("cls");
    int average;
    string result;
    cout<<"Input the value:";
    cin>>average;
    // if(average>=50){
    //     result="pass";
    // }
    // else{
    //     result="fail";
    // }
    /*A ternary operator is a shorthand way of writing an if-else statement in a single line. */
    // condition ? block_true : block_false
    result=(average>=50 ? "pass":"fail");
    cout<<"Your average:"<<average<<endl;
    cout<<"Your result:"<<result<<endl;
    return 0;
}