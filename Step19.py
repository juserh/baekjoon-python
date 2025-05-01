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

#Q25501
import sys

def recursion(st, l, r) :
    global cnt #전역변수
    cnt += 1
    if l >= r :
        return [1, cnt]
    elif s[l] != s[r] :
        return [0, cnt]
    else :
        return recursion(st, l+1, r-1)

def isPalindrome(st) :
    return recursion(st, 0, len(st)-1)

t = int(sys.stdin.readline())

for _ in range(t) :
    cnt = 0
    s = sys.stdin.readline().rstrip()
    print(*isPalindrome(s))