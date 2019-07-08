vjj,vkk=map(int,input().split())
list1=list(map(int,input().split()))
vjj=[]
list1.insert(0,0)
for y in range(vkk):
     v=[]
     sumup=0
     cc,dd=map(int,input().split())
     for i in range(cc,dd+1):         
         sumup^=list1[i]     
     vjj.append(sumup)
for y in vjj:
    print(y)
