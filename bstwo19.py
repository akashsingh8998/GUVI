# your code goes here
n = int(input())
fact = 1
if (n==0 or n==1):
	fact = 1
else:
	for i in range(2,n+1):
		fact *= i
print(fact)
