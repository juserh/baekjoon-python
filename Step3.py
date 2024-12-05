#Q2739
a = int(input())
for i in range(1,10):
    print(a, "*", i, "=", a*i)

#Q10950
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    print(a+b)

#Q8393
a = int(input())
total = 0
for i in range(1, a+1):
    total += i
print(total)

#Q25304
x = int(input())
n = int(input())
total = 0
for i in range(n):
    a, b = map(int, input().split())
    total += a*b
if (total == x): print("Yes")
else: print("No")

#Q25314
a = int(input())
a = a//4
s=""
for i in range(a):
    s += "long "
s += "int"
print(s)

#Q15552
# 시간 초과 시, input 대신 sys.stdin.readline
# 문자열을 저장하고 싶을 경우 .rstrip()을 추가로
import sys
t = int(input())
for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)

#Q11021
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    print(f'Case #{i+1}: {a+b}')

#Q11022
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    print(f'Case #{i + 1}: {a} + {b} = {a + b}')

#Q2438
n = int(input())
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print("")

#Q2439
n = int(input())
for i in range(n):
    star = ""
    for j in range(n-i-1):
        star += " "
    for k in range(i+1):
        star += "*"
    print(star)

#Q10952
while (1):
    a, b = map(int, input().split())
    if(a==0 and b==0):
        break
    print(a+b)

#Q10951
while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break