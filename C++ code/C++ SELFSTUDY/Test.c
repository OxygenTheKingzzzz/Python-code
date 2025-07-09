// #include<stdio.h>
// int main(){
//     printf("Hello World!!!!!!");
//     return 0;
// }
// #include <stdio.h>

// int main() {
//     char name[10], color[20], funfact[50];
//     int age;

//     printf("Enter your name: ");
//     scanf("%s", name);

//     printf("Enter your age: ");
//     scanf("%d", &age);
//   // Fix: Consume the leftover newline

//     printf("Enter your color: ");\
//     scanf("%s", color);

//     printf("Enter a fun fact: ");
//     scanf(" %[^\n]", funfact);  // Fix: Reads full line with spaces

//     printf("\nHello! My name is %s.\n", name);
//     printf("I am %d years old.\n", age);
//     printf("My favorite color is %s.\n", color);
//     printf("Fun fact: %s\n", funfact);

//     return 0;
// }
#include <stdio.h>
int main(){
    char myName[50];
    scanf("%s", myName);
    printf("Hello %s", myName);
    return 0;

}