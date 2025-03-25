# #Q1934
# t = int(input())
# for _ in range(t) :
#     a, b = map(int, input().split())
#
#     result = a*b
#     while b>0 :
#         a, b = b, a%b
#     print(result // a)
# """
# #내장 라이브러리
# import math
# for _ in range(t) :
#     a,b = map(int, input().split())
#     print(math.lcm(a,b))
# """

# #Q13241
# a, b = map(int, input().split())
# result = a*b
# while b > 0 :
#     a, b = b, a%b
# print(result//a)

# #Q1735
# def gcd(x1, x2) :
#     while x2 > 0 :
#         x1, x2 = x2, x1 % x2
#     return x1
# a1, a2 = map(int, input().split())
# b1, b2 = map(int, input().split())
# s1 = b2 * a1 + a2 * b1
# s2 = a2 * b2
# n = gcd(s1, s2)
# print(s1//n, s2//n)

# #Q2485
# def gcd_count(li) :
#     a = li[0]
#     for i in range(1,n-1) :
#         b = li[i]
#         while b > 0 :
#             a, b = b, a%b
#     sum = 0
#     for l in li :
#         sum += (l//a-1)
#     return sum
#
# n = int(input())
#
# arr = [int(input()) for _ in range(n)]
# dis = [(arr[i]-arr[i-1]) for i in range(1,n)]
# print(gcd_count(dis))

# #Q4134
# import sys
# def is_decimal(num) :
#     for i in range(2, int(num**0.5)+1) :
#         if num%i == 0 :
#             return False
#     return True
#
# n = int(sys.stdin.readline())
# for _ in range(n) :
#     a = int(sys.stdin.readline())
#     r = False
#     while not r:
#         if a==0 or a==1 :
#             print(2)
#             break
#         r = is_decimal(a)
#         if not r:
#             a += 1
#         else :
#             print(a)
#             break

# #Q1929
# import sys
# def is_decimal(num) :
#     if num == 1 : return False
#     for i in range(2, int(num**0.5)+1) :
#         if num%i == 0 :
#             return False
#     return True
# m, n = map(int, sys.stdin.readline().split())
#
# for i in range(m, n+1) :
#     r = is_decimal(i)
#     if r :
#         print(i)

# #Q4948
# import sys
# num = 123456 *2 +1
# arr = [1]* num
# for i in range(num) :
#     if num == 1 : continue
#     for j in range(2, int(i**0.5)+1) :
#         if i%j == 0 :
#             arr[i] = 0
#             break
#
# while True :
#     n = int(sys.stdin.readline())
#     if n == 0 :
#         break
#     else :
#         print(sum(arr[n+1:2*n+1]))

# #Q17103
# import sys
# decimals = []
# check = [0] * 1000001
# check[0] = 1
# check[1] = 1
# for i in range(2, 1000001) :
#     if check[i] == 0 :
#         decimals.append(i)
#         for j in range(2*i, 1000001, i) :
#             check[j] = 1
#
# t = int(sys.stdin.readline())
# for _ in range(t) :
#     n = int(sys.stdin.readline())
#     cnt = 0
#     for d in decimals :
#         if d > n//2 :
#             break
#         if not check[n-d] :
#                 cnt += 1
#     print(cnt)

#Q13909
n = int(input())
print(int(n**0.5))