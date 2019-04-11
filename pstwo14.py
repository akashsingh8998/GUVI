# your code goes here
import re
n=int(input())
z=input()
t=re.sub('[aeiou]','',z)
print(t[::-1])
