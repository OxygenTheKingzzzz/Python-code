#include<iostream>
using namespace std;
int main (){
    system("cls");
    int n;
    cout<<"Insert How Many Names You Want To Insert: ";cin>>n;
    cin.ignore();
    string word[n];
    cout<<"Insert "<<n<<" Name"<<endl;
    for(int i = 0; i < n; i++){
        cout<<i+1<<" ";getline(cin,word[i]);
        }
    int size = sizeof(word)/sizeof(word[0]);
    for (int i = 0; i < size; i++){
        for (int j = 0; j < size - i - 1; j++){
            if (word[j] > word[j+1]){
                string temp = word[j];
                word[j] = word[j + 1];
                word[j + 1] = temp;
            }
        }
    }
    system("cls");
    cout<<"Letter-based Name on A-Z:"<<endl;
    for (int i = 0; i < n; i++){
        cout<<i+1<<" "<<word[i]<<endl;
    }

}