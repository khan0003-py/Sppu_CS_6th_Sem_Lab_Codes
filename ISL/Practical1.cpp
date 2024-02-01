/*
Write a C++ program that contains a string (char pointer) with a value \Hello World’. The program should AND or and XOR each character in this string with 127 and display the result.
*/

#include<iostream>
using namespace std;
int main(){

	char *str = "Hello World";
	cout<<"Original String : "<<str<<endl;

	cout<<"AND Result :";
	for(int i=0; str[i] != '\0'; i++){
		cout<<(char)(str[i]&127);
	}

	cout<<endl;

	cout<<"XOR Result :";
	for(int i=0; str[i] != '\0'; i++){
		cout<<(char)(str[i]^127);
	}

	return 0;
}

