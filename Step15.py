#Q1934
t = int(input())
for _ in range(t) :
    a, b = map(int, input().split())

    result = a*b
    while b>0 :
        a, b = b, a%b
    print(result // a)
"""
#내장 라이브러리
import math
for _ in range(t) :
    a,b = map(int, input().split())
    print(math.lcm(a,b))
"""
