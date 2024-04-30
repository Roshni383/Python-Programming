# profit=[10,5,15,7,6,18,3]
# weight=[2,3,5,7,1,4,1]
# capacity=15
# pro=[]
# for i in range(len(profit)):
#         pro.append("{:.1f}".format(profit[i]/weight[i]))
# vis=[]
# for j in range(len(pro)):
#     maxi=max(pro)
#     s=weight[pro.index(maxi)]
#     capacity-=s
#     pro[pro.index(maxi)] = 0
#     print(pro)
#
profit = [10, 5, 15, 7, 6, 18, 3]
weight = [2, 3, 5, 7, 1, 4, 1]
capacity = 15
balance=capacity
pro = []
sumi=0
for i in range(len(profit)):
    pro.append(profit[i] / weight[i])
print(pro)
for j in range(len(pro)):
    maxi = max(pro)
    s = weight[pro.index(maxi)]
    capacity -= s
    if capacity>0:
        sumi += profit[pro.index(maxi)]
        pro[pro.index(maxi)] = 0
        print(pro)
        balance-=s
    else:
        sumi += balance * pro[pro.index(maxi)]
        pro[pro.index(maxi)] = 0
        print(pro)
        break
print(sumi,balance)

