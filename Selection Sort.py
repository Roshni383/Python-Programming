ar = list(map(int, input().split()))
n = len(ar)
min1 = 0
for j in range(n):
    min1 = j
    for i in range(j + 1, n):
        if ar[i] < ar[min1]:
            min1 = i
        ar[j], ar[min1] = ar[min1], ar[j]
print(ar)
