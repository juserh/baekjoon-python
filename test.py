import sys

def select(idx, cnt) :
    global arr, n, total

    for j in range(idx, n) :
        if idx+3 <= n-1 :
            select(idx+3, cnt+arr[j])
        else :
            total.append(cnt+arr[j])
            return

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

total = []
for i in range(n) :
    cnt = arr[i]
    if i+3 <= n-1 :
        select(i+3, cnt)
    else :
        total.append(cnt)

print(max(total))