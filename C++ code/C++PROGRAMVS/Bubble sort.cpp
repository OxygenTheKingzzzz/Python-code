#include<iostream>
using namespace std;
int main(){
    int number[]={54,454,-34,67,-122,664,458,-24,211,500,44434,};
    int length =sizeof(number)/sizeof(number[0]);
    for(int i=0;i<length; i++){
    for(int j=0;j<length-1; j++){
        if(number[j]>number[j+1]){
            int temp = number[j];
            number[j]= number[j+1];
            number[j+1]=temp;
        }
    }
    }
    cout<<"Sorted array in ascending order:";
    for(int i=0; i<length ;i++){
        cout << number[i] << " ";

    }
return 0;
}
