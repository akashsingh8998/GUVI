# your code goes here
string = input()
t = list(set(string))
a = []
for i in t:
    a.append(string.count(i))
print(t[a.index(max(a))])
