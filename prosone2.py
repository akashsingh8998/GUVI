# your code goes here
def reduction(n,k):
   if k<=0:
     return n
   if n==0:
     return 10
   a=reduction(n//10,k)*10+n%10
   a1=reduction(n//10,k-1)
   if a<a1:
     return a
   else: 
     return a1
n,k=input().split()
n,k=int(n),int(k)
print(reduction(n,k))
