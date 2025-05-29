import sys
from collections import deque

def bfs(y, x) :
    global n, board, visited
    q = deque()
    q.append([y, x])

    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]
    color = board[y][x]
    while q :
        cy, cx = q.popleft()

        for dyy, dxx in zip(dy, dx) :
            ny = cy + dyy
            nx = cx + dxx
            if 0<=ny<n and 0<=nx<n and visited[ny][nx] == 0 :
                if board[ny][nx] == color :
                    visited[ny][nx] = 1 #방문 표시
                    q.append([ny, nx])
    return


n = int(sys.stdin.readline())
board = []
for _ in range(n) :
    row =  list(sys.stdin.readline().rstrip())
    board.append(row)

visited = [[0]*n for _ in range(n)]
cnt_none = 0
for i in range(n) :
    for j in range(n) :
        if visited[i][j] == 0 :
            bfs(i, j)
            cnt_none += 1

for i in range(n) :
    for j in range(n) :
        if board[i][j] == "G" :
            board[i][j] = "R"
visited = [[0]*n for _ in range(n)]
cnt_RG = 0
for i in range(n) :
    for j in range(n) :
        if visited[i][j] == 0 :
            bfs(i, j)
            cnt_RG += 1

print(cnt_none, cnt_RG)