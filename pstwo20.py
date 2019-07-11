# your code goes here
s = input()
a = []
for i in range(0,len(s)):
	a.append(s[i])
for i in range(0,len(a)):
	a[i] = chr(((ord(a[i])+3-64)%26)+64)
print("".join(a))	
