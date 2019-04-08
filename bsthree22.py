# your code goes here
n = int(input())
a = []
b = input().split()
for i in range(0,n):
	a.append(int(b[i]))
print(max(a))
