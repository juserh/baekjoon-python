#Q2798
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)

total_m = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1, n):
            total = arr[i] + arr[j] + arr[k]
            if (total<=m) and (total>total_m):
                total_m = total
print(total_m)

#Q2231
