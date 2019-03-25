# your code goes here
n,k = input().split()
n = int(n)
k = int(k)
a = []
for j in range (n+1,k):
	temp = j
	sum = 0
	while(j>0):
		rem = j % 10
		sum += rem ** 3
		j = j // 10
	if(sum==temp):
		a.append(str(temp))
print(" ".join(a))
