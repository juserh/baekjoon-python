import sys

n = int(sys.stdin.readline())
arr = [0]
for _ in range(n) :
    arr.append(int(sys.stdin.readline()))

dp = [0]*(n+1)
if len(arr) <= 2 :
    print(sum(arr))
else :
    dp = [0, arr[1], arr[1]+arr[2]]
    for i in range(3, n+1) :
        dp.append(max(arr[i]+arr[i-1]+dp[i-3], arr[i]+dp[i-2]))
    print(dp[n])