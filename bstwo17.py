# your code goes here
n = int(input())
temp = n
sum = 0
while(n>0):
	rem = n % 10
	sum += rem ** 3
	n = n // 10
if(sum == temp):
	print("yes")
else:
	print("no")
