# your code goes here
a = int(input())
n = []
t = input().split()
for i in range(0,a):
	n.append(int(t[i]))
for i in range(0,a):
	for j in range(i+1,a):
		if(n[i]+n[j] == 0):
			print(n[i],n[j])
			break
