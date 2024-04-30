lst1=['1','3','4','5','6','8','9']
lst2=['1','5','8','9','2']
intersect=[]
expect=[]
union=lst1+lst2
union=set(union)
for ele in lst1:
    if ele in lst2:
        intersect.append(ele)
    else:
        expect.append(ele)
        print(expect)
for i in range(len(lst1)):
    if lst1[i]%2!=0:
        expect.append(lst1[i])
    if lst2[i]%2==0:
        expect.append(lst2[i])
print(*union)
print(*intersect)
print(*expect)