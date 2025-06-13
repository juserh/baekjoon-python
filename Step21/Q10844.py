import sys

n = int(sys.stdin.readline())
nums = [[0]*10 for i in range(n)]
nums[0] = [0,1,1,1,1,1,1,1,1,1]

for i in range(1, n) :
    for idx in range(10) :
        if idx - 1 >= 0 :
            nums[i][idx-1] += nums[i-1][idx]
        if idx + 1 < 10 :
            nums[i][idx+1] += nums[i-1][idx]

print(sum(nums[n-1])%1000000000)