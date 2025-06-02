import sys

n = int(sys.stdin.readline())

cnt = 0
if n < 100 :
    cnt = n
else :
    cnt += 99
    for num in range(100, n+1) :
        s = list(map(int, str(num)))
        d = s[1] - s[0]
        for i in range(1, len(s)) :
            if s[i] != s[i-1] + d :
                break
        else :
            cnt += 1
print(cnt)

"""
#문제 조건 n<=1000을 반영한 풀이
import sys

n = int(sys.stdin.readline())

cnt = 0
if n < 100 :
    cnt = n
else :
    cnt += 99
    for num in range(100, n+1) :
        s = list(map(int, str(num)))
        d1 = s[1] - s[0]
        d2 = s[2] - s[1]
        if d2 == d1 :
            cnt += 1
print(cnt)
"""