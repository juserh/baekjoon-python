#Q1037
import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
mx = max(arr)
mn = min(arr)
print(mx*mn)
