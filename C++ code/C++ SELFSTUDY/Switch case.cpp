#include<iostream>
using namespace std;
int main(){
    system("cls");
    int day;
    cout<<"Please input the number:"<<endl;
    cin>>day;
    switch(day){
        case 1:
        cout<<"Today is Monday"<<endl;
        break;
        case 2:
        cout<<"Today is Tuesday"<<endl;
        break;
        case 3:
        cout<<"Today is Wednesday"<<endl;
        break;
        case 4:
        cout<<"Today is Thursday"<<endl;
        break;
        case 5:
        cout<<"Today is Friday"<<endl;
        break;
        case 6:
        cout<<"Today is Saturday"<<endl;
        break;
        case 7:
        cout<<"Today is Sunday"<<endl;
        break;
    }
    return 0;
}