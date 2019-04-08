#include <iostream>
#include <string>
using namespace std;
 
int main() {
	// your code goes here
	string str1;
	string str2(".");
	cin>>str1;
	str1.append(str2);
	cout<<str1;
	return 0;
}
