# your code goes here
n = int(input())
a = []
for j in range(n):
	k = input()
	a.append(k)
word = "kabali"
word = sorted(word)
count = 0
for i in a:
	i = sorted(i)
	if(i == word):
		count += 1
print(count)
