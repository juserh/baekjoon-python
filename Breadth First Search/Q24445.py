import sys
from collections import deque

def bfs(r) :
    global visited
    global line

    cnt = 1
    q = deque([r])
    visited[r] = cnt
    while q :
        current = q.popleft()

        if line[current] :
            arr = sorted(line[current], reverse=True)
            for a in arr :
                if visited[a] == 0 :
                    q.append(a)
                    cnt += 1
                    visited[a] = cnt


n, m, r = map(int, sys.stdin.readline().split())
line = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m) :
    u, v = map(int, sys.stdin.readline().split())
    line[u].append(v)
    line[v].append(u)

bfs(r)
for i in range(1, n+1) :
    print(visited[i])