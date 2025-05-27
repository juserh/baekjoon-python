import sys
from collections import deque

def bfs(ch, cw) :
    global geo, w, h
    q = deque()
    q.append([ch, cw])

    dw = [-1, 0, 1, -1, 1, -1, 0, 1]
    dh = [-1, -1, -1, 0, 0, 1, 1, 1]
    while q :
        hh, ww = q.popleft()
        for k in range(8) :
            nh = hh + dh[k]
            nw = ww + dw[k]

            if 0<=nw<w and 0<=nh<h and geo[nh][nw] == 1 :
                q.append([nh, nw])
                geo[nh][nw] = 0

sys.setrecursionlimit(10000)
def dfs(ch, cw) :
    global geo, w, h

    dw = [-1, 0, 1, -1, 1, -1, 0, 1]
    dh = [-1, -1, -1, 0, 0, 1, 1, 1]
    geo[ch][cw] = 0
    for k in range(8) :
        nh = ch+ dh[k]
        nw = cw + dw[k]

        if 0 <= nw < w and 0 <= nh < h and geo[nh][nw] == 1:
            dfs(nh, nw)


while True :
    w, h = map(int, sys.stdin.readline().split())

    if w ==0 and h == 0 :
        break
    geo = []
    for _ in range(h) :
        g = list(map(int, sys.stdin.readline().split()))
        geo.append(g)

    cnt = 0

    for i in range(h) :
        for j in range(w) :
            if geo[i][j] == 1 :
                dfs(i, j)
                cnt += 1

    print(cnt)