#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int K,N,i,sum=0;
	cin>>N>>K;
	int a[N];
	for(i=0; i<N; i++)
	{
		cin>>a[i];
	}
	for(i=0;i<K;i++)
	{
		sum += a[i];
	}
	cout<<sum;
	return 0;
}
