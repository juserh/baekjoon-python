import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    global n, m
    global cnt, visited, campus

    # 범위를 벗어나면 종료
    if x < 0 or x >= n or y < 0 or y >= m:
        return
    # 이미 방문했거나 벽이라면 종료
    if visited[x][y] == 1 or campus[x][y] == 'X':
        return

    visited[x][y] = 1
    if campus[x][y] == 'P':
        cnt += 1

    # 상하좌우로 탐색
    dfs(x-1, y)
    dfs(x+1, y)
    dfs(x, y-1)
    dfs(x, y+1)

n, m = map(int, sys.stdin.readline().split())
campus = []
X, Y = 0, 0
for i in range(n) :
    row = sys.stdin.readline().rstrip()
    campus.append(row)
    if 'I' in row :
        Y = row.find('I')
        X = i

visited = [[0] * m for _ in range(n)]
cnt = 0

dfs(X, Y)
if cnt == 0 :
    print("TT")
else :
    print(cnt)