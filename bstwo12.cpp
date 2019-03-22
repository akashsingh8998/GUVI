#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int N,temp,rev,val;
	cin>>N;
	temp = N;
	rev = 0;
	while(N>0)
	{
		val = N % 10;
		rev = rev * 10 + val;
		N = N / 10;
	}
	if(temp==rev)
	{
		cout<<"yes";
	}
	else
	{
		cout<<"no";
	}
	return 0;
}
