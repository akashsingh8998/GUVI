# your code goes here
ch = input()
if (ch>="a" and ch<="z") or (ch>="A" and ch<="Z"):
	if ch in ('a','A','e','E','i','I','o','O','u','U'):
		print("Vowel")
	else:
		print("Consonant")
else:
	print("invalid")
