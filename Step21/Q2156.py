import sys

n = int(sys.stdin.readline())
bottles = [0] * 10001
for i in range(1, n+1) :
    bottles[i] = int(sys.stdin.readline())

dp = [0] * 10001
dp[1] = bottles[1]
dp[2] = bottles[2]+bottles[1]

for i in range(3, n+1) :
    dp[i] = max(bottles[i] + bottles[i-1] + dp[i-3], bottles[i] + dp[i-2], dp[i-1] )

print(max(dp))