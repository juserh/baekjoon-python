import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

total = arr.copy()
for idx in range(1, n):
    total[idx] = max(total[idx], total[idx]+total[idx-1])
print(max(total))
print(total)