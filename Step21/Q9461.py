import sys

t = int(sys.stdin.readline())
arr = [0,1,1,1,2,2]

for i in range(6, 101) :
    arr.append(arr[i-5]+arr[i-1])
for _ in range(t) :
    n = int(sys.stdin.readline())
    print(arr[n])