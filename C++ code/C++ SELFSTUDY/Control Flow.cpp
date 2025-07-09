/*The following code is about else*/
// #include<iostream>
// using namespace std;
// int main(){
//     system("cls");
//     int x;
//     cout<<"Enter the value:";
//     cin>>x;
//     if(x>50){
//         cout<<"The value is greater than 50!!"<<endl;
//     }
//     if(x<50){
//         cout<<"The value is less than 50!!"<<endl;
//     }
//     if(x==50){
//         cout<<"It's equal 50!!"<<endl;
//     }
//     return 0;
// }
/*The following code is about if and else if*/
// #include<iostream>
// using namespace std;
// int main(){
// system("cls");
// float product_price;
// cout<<"Enter the value:";
// cin>>product_price;
// if(product_price>=50){
//     cout<<"You get a 20$ voucher!!";
// }
// else{
//     cout<<"Try again next time";
// }
// return 0;
// }
/*The following code is about if, if else and if else if*/
#include<iostream>
using namespace std;
int main(){
    system("cls");
    double product_price;
    cout<<"Enter the product price:";
    cin>>product_price;
    if(product_price>=20 && product_price<=40){
        cout<<"Discount 15%";
    } 
    else if(product_price>=41 && product_price<=60){
        cout<<"Discount 30%";
    }
    else if(product_price>61){
        cout<<"Discount 50%";
    }
    else{
        cout<<"Nothing";
    }
}
