#include <iostream>
#include<string>
using namespace std;
int main(){
    system("cls");
    int size;
     cout<<"[+]Insert number of freshmen: "<<endl;
     cin>>size;
     string studentName[size];
    while (true){
        cout<<"==========================================Freshmen of our university=========================================="<<endl;
        cout<<"1.List all students' name"<<endl;
        cout<<"2.Add new students' name"<<endl;
        cout<<"3.Update students's name by inserting the new one"<<endl;
        cout<<"4.Exit"<<endl;
        cout<<"==========================================Oxygen University of Konoha=========================================="<<endl;
    
        int opt;
        cout<<"[+]Insert option"<<endl;
        cin>>opt;
        switch (opt)
        {
        case 1:
        system("cls");
        cout<<"1.List all students' name"<<endl;
        for (string n: studentName){
        if(n.length()==0) {
        cout<<"!no student's name"<<endl;
        }
        for(string name:studentName){
            cout<<"student"<<endl;

        }
        }
         break;
        case 2:
        system("cls");
        cout<<"2.Add new students' name"<<endl;
        int index;
        cout<<"[+]Insert student's index"<<endl;
        cin>>index;
        if (studentName[index]!=""){
        cout<<"This name already existed"<<endl;
        }
        else {
            string sn;
            cout<<"Insert new student's name"<<endl;
            cin.ignore();
            getline(cin,sn);
            studentName[index]=sn;
                cout<<"student's name " + sn <<" inserted sucessfully"<<endl;
            }
            break;
            case 3:
            system("cls");
            cout<<"Update student's list"<<endl;
            cout<<"[+]Insert student index:"<<endl;
            cin>>index;
            if(index<1 || index> size){
                cout<<"Invalid"<<endl;
            }
                else if(index>=0 || index == size){
                   
                    string studentName;
                    cout<<"[+]Insert student name:"<<endl;
                    cin.ignore();
                    getline(cin,studentName);
                    cout<<"List updating:"<<studentName[index-1]<<endl;
                    
                    }
                    else{
                        cout<<"Current name:"<<studentName[index-1]<<endl;
                        cout<<"[+]Insert new name:"<<endl;
                        cin.ignore();
                        getline(cin,studentName[index-1]);
                        cout<<"update sucessfully"<<endl;

                    }
            break;
            default:
    
            cout<<"exit"<<endl;
             }
              }
              return 0;
}