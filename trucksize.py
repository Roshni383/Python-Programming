
boxTypes = [[5,10],[2,5],[4,7],[3,9]]
# boxTypes = [[1,3],[2,2],[3,1]]
s= sorted(boxTypes, key=lambda x:x[1],reverse=True)
print(s)
unit = 0
truckSize=10
t = truckSize
for a, b in s:
    if t < 0:
        break
    else:
        if t != 0:
            if a < t:
                unit += (a * b)
                print(unit)
                t -= a
                print(t)
            else:
                unit += (t * b)
                print(unit)
                t -= a
                print(t)
print(unit)



