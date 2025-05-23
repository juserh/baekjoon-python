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

# #Q4779
# import sys
#
# def transform(num) :
#     if num == 1 :
#         return "-"
#     else :
#         d = num // 3
#         left = transform(d)
#         center = " " * d
#         return left + center + left
#
# while True :
#     try:
#         n = int(sys.stdin.readline().rstrip())
#         n = 3**n
#         s = transform(n)
#         print(s)
#     except :
#         break

# #Q2447
# import sys
#
# def star(num) :
#     if num == 1 :
#         return ['*']
#
#     pre = star(num//3)
#     result = []
#
#     for p in pre :
#         result.append(p*3)
#     for p in pre :
#         result.append(p+' '*(num//3)+p)
#     for p in pre :
#         result.append(p*3)
#
#     return result
#
# n = int(sys.stdin.readline())
# result = star(n)
#
# print('\n'.join(result))

#Q11729
import sys

def hanoitop(num, current, next) :
    if num == 1 :
        print(current, next)
        return
    hanoitop(num-1, current, 6-current-next) #1단계: n-1개를 1->2
    print(current, next) #2단계: 마지막 n번째 원판 1->3
    hanoitop(num-1, 6-current-next, next) #3단계: n-1개를 2->3

n = int(sys.stdin.readline())
print(2**n-1)
hanoitop(n, 1, 3)