# your code goes here
n,k = input().split()
n = int(n)
k = int(k)
a = []
for j in range (n+1,k):
	flag = 1
	for i in range(2,j):
		if(j%i==0):
			flag = 0
			break
	if(flag==1):
		a.append(str(j))
print(" ".join(a))
