n=int(input("Enter the no of buildings"))
Hi=list(map(int,input().split()))
subset1=[]
subset2=[]
sum1=0
for i in range(n):
    for j in range(i+1,n+1):
        subset1.append(Hi[i:j])
        subset2.append(Hi[j:n+1])
        for ele in subset1:
            sum1+=ele
        for ele in subset2:
            sum2+=ele



print(subset1)
print(subset2)
