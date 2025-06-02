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