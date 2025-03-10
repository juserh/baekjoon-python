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

#Q4134
import sys
def is_decimal(num) :
    for i in range(2, int(num**0.5)+1) :
        if num%i == 0 :
            return False
    return True

n = int(sys.stdin.readline())
for _ in range(n) :
    a = int(sys.stdin.readline())
    r = False
    while not r:
        if a==0 or a==1 :
            print(2)
            break
        r = is_decimal(a)
        if not r:
            a += 1
        else :
            print(a)
            break

