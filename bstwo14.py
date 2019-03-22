# your code goes here
N,Q = input().split()
N = int(N)
Q = int(Q)
for i in range(N+1,Q):
	if(i%2==1):
		print(i,end=" ")
