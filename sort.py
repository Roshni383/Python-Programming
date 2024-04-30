n=int(input())
prices=list(map(int,input().split()))
org=prices
dup=sorted(prices)
ind=1
partitions=[]
while len(org)>0:
    if sorted(org[:ind])==dup[:ind]:
        partitions.append(dup[:ind])
        org=org[ind:]
        dup=dup[ind:]
        ind=1
    else:
        ind+=1
print(partitions)
