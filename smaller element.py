n=int(input())
n=list(map(int,input().split()))
count=0
res=[]
for i in range(len(n)-1):
    for j in range(i+1,len(n)):
        if n[i]>n[j]:
            count=count+1
    res.append(count)
    count=0
res.append(0)
print(*res)