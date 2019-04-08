# your code goes here
text1,text2 = input().split()

for index, letter in enumerate(text1):
    text1 = text1.replace(letter, str(index))
    
for index, letter in enumerate(text2):
    text2 = text2.replace(letter, str(index))

if(text1==text2):
	print("yes")
else:
	print("no")
