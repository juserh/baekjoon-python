#Q2798
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)

total_m = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1, n):
            total = arr[i] + arr[j] + arr[k]
            if (total<=m) and (total>total_m):
                total_m = total
print(total_m)

#Q2231
n = int(input())

for i in range(1,n+1):
    num = sum((map(int, str(i))))
    num_sum = i+num
    if num_sum == n:
        print(i)
        break
    if i ==n :
        print(0)

#Q19532
a,b,c,d,e,f = map(int,input().split())
for x in range(-999,1000):
    for y in range(-999, 1000):
        if (a*x + b*y == c) and (d*x + e*y == f):
            print(x, y)
            break

#Q1018
n, m = map(int, input().split())
board = []
result = []

for _ in range(n):
    board.append(input())

for i in range(n-7): #가로
    for j in range(m-7): #세로
        is_black = 0 #검은색 시작
        is_white = 0 #흰색 시작

        #8*8보드
        for a in range(i, i+8) :
            for b in range(j, j+8) :
                if (a+b)%2 == 0 : # board[짝수][짝수] or board[홀수][홀수]
                    if board[a][b] !='B':
                        is_black += 1
                    if board[a][b] != 'W':
                        is_white += 1
                else :
                    if board[a][b] != 'W':
                        is_black += 1
                    if board[a][b] != 'B':
                        is_white += 1
        result.append(min(is_black, is_white))
print(min(result))

#Q1436
n = int(input())

i = 1
snum = 666
while i != n :
    snum += 1
    if '666' in str(snum) :
        i += 1

print(snum)

#Q2839
n = int(input())
cnt = 0

while n>=0 :
    if n%5 == 0 :
        cnt += n//5
        print(cnt)
        break
    n -= 3
    cnt += 1
if n < 0 :
    print(-1)
