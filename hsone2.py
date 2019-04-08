# your code goes here
n = int(input())
a = []
b = input().split()
for i in range(0,n):
	a.append(b[i])
a = sorted(a)[::-1]
print("".join(a))
