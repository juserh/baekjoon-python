# #Q27433
# import sys
# def factorial(num) :
#     if num <=1 :
#         return 1
#     return factorial(num-1)*num
#
# n = int(sys.stdin.readline())
# print(factorial(n))

# #Q10870
# import sys
# def fibo(num) :
#     if num <= 1 :
#         return num
#     return fibo(num-1) + fibo(num-2)
#
# n = int(sys.stdin.readline())
# print(fibo(n))

# #Q25501
# import sys
#
# def recursion(st, l, r) :
#     global cnt #전역변수
#     cnt += 1
#     if l >= r :
#         return [1, cnt]
#     elif s[l] != s[r] :
#         return [0, cnt]
#     else :
#         return recursion(st, l+1, r-1)
#
# def isPalindrome(st) :
#     return recursion(st, 0, len(st)-1)
#
# t = int(sys.stdin.readline())
#
# for _ in range(t) :
#     cnt = 0
#     s = sys.stdin.readline().rstrip()
#     print(*isPalindrome(s))

# #Q24060
# import sys
#
# def merge_sort(li) :
#     global saved
#
#     if len(li) == 1 :
#         return li
#
#     mid = (len(li)+1) // 2
#
#     left = merge_sort(li[:mid])
#     right = merge_sort(li[mid:])
#
#     i, j = 0, 0
#
#     tmp = []
#     while (i< len(left) and j< len(right)) :
#         if left[i] <= right[j] :
#             tmp.append(left[i])
#             i += 1
#         else :
#             tmp.append(right[j])
#             j += 1
#
#     while i<len(left) :
#         tmp.append(left[i])
#         i += 1
#     while j<len(right):
#         tmp.append(right[j])
#         j += 1
#
#     for t in tmp :
#         saved.append(t)
#     return tmp
#
# n, k = map(int, sys.stdin.readline().split())
# a = list(map(int, sys.stdin.readline().split()))
#
# saved = []
# merge_sort(a)
# if len(saved) < k :
#     print(-1)
# else :
#  print(saved[k-1])

#Q4779
import sys

def transform(num) :
    if num == 1 :
        return "-"
    else :
        d = num // 3
        left = transform(d)
        center = " " * d
        return left + center + left

while True :
    try:
        n = int(sys.stdin.readline().rstrip())
        n = 3**n
        s = transform(n)
        print(s)
    except :
        break