#include<iostream>
using namespace std;
int main(){
    int s;
    cout<<"[+]Insert number of name:";
    cin>>s;
    cin.ignore();
    string name[s];
    cout<<"insert"<<s<< "name"<<endl;
    
    for(int i=0;i<s;i++){
        cout<<i+1<<" ";
        getline(cin,name[s]);
    }
    int size = sizeof(name)/sizeof(name[0]);
    for(int i =0 ;i<size ;i++){
    for(int j= 0;j<size-i-1;j++){
    if(name[j]>name[j+1]){
        string temp= name[j];
        name[j] = name[j+1];
        name[j+1]= temp;
    }
    }

    }
    cout<<"This is the ordered name"<<endl;
    for(int i=0;i<s;i++){
        cout<<i+1<<"   "<<name[i]<<endl;
    } 
    return 0;
}