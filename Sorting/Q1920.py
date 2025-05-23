import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr = sorted(arr)

m = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

for num in nums :
    start, end = 0, n-1
    exist = 0

    while start <= end :
        mid = (start + end) // 2

        if arr[mid] == num :
            exist = 1
            print(1)
            break
        if num > arr[mid] :
            start = mid + 1
        else :
            end = mid -1
    if exist == 0 :
        print(0)