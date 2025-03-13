n = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)
total = 0
for i in range(1, n+1) :
    total += sum(arr[0:i])
print(total)