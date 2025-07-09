#include<iostream>
using namespace std;
int main(){
    string names[]={"Sak","Nha","Ro", "chill guy"};
    cout<<"All name"<<endl;
    for(string i: names){
        cout<<i<<" ";
    }
cout<<"\n[+]Insert name to delete"<<endl;
string name;
getline(cin,name);
int size= sizeof(names)/sizeof(names[0]);
for(int i=0; i<size;i++){
    if(names[i]==name){
        names[i]="";
        break;
    }
}
cout<<"name after deleted"<<endl;
for(string i:names){
if(i!=""){
cout<<i<<endl;
}
}
return 0;
}