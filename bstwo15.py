# your code goes here
N,Q = input().split()
N = int(N)
Q = int(Q)
if(N+4 == Q):
	for i in range(N+1,Q):
		if(i%2==0):
			print(i,end="")
else:
	for i in range(N+1,Q-1):
		if(i%2==0):
			print(i,end=" ")
	for i in range(Q-1,Q):
		if(i%2==0):
			print(i,end="")
