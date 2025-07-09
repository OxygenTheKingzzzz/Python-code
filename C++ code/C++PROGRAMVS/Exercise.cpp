#include<iostream>
#include<string>
using namespace std;

int main(){
    system("cls");
    /** 
     * Create a system to insert students' name
     * This system contains 4 options
     * 1. List all students' name
     * 2. Add new student's name
     * 3. Update student's name by inserting the old name
     * 4. Exit
    */
   int size;
   cout<<"[+] Insert number of students' name to set up system: ";cin>>size;
   string studentName[size];
   while (true){
        cout<<"======== Student management System ==========\n";
        cout<<"1. List students"<<endl;
        cout<<"2. Add new student\n";
        cout<<"3. Update student's name by old name\n";
        cout<<"4. Exit\n";
        cout<<"=============================================\n";
        int opt;
        cout<<"[+] Insert option: ";cin>>opt;
        switch(opt){
            case 1:
                system("cls");
                cout<<"+ List all students option:\n";
                for(string n: studentName){
                    if(n.length()==0){
                        cout<<"[!] No student name.\n";
                    }
                }
                for(string name: studentName){
                    cout<<"Student: "<<name<<endl;
                }
                break;
            case 2:
                system("cls");
                cout<<"+ Insert student name option: \n";
                int index;
                cout<<"[+] Insert student's name index: ";cin>>index;
                if(studentName[index]!=""){
                    cout<<"This is index already existed\n";
                }else{
                    string sn;
                    cout<<"[+] Insert student's name: ";
                    cin.ignore();
                    getline(cin, sn);
                    studentName[index] = sn;
                    cout<<"[+] Student name " + sn <<" has been inserted succesfully.\n";
                }
                break;
            default: 
                cout<<"[!] Invalid option\n";
        };
   }
   
    return 0;
}