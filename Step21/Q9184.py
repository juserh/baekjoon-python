import sys

def w(a, b, c) :
    global dp

    if a<=0 or b<=0 or c<=0 :
        return 1
    if a>20 or b>20 or c>20 :
        return w(20,20,20)
    if dp[a][b][c] :
        return dp[a][b][c]
    if a<b and b<c :
        dp[a][b][c] = w(a,b,c-1) +w(a,b-1,c-1) -w(a,b-1,c)
    else :
        dp[a][b][c] = w(a-1,b,c) +w(a-1,b-1,c) +w(a-1,b,c-1) -w(a-1,b-1,c-1)
    return dp[a][b][c]


dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]
while True :
    x, y, z = map(int, sys.stdin.readline().split())

    if x==-1 and y==-1 and z==-1 :
        break
    result = w(x, y, z)
    print(f'w({x}, {y}, {z}) = {result}')




