import sys
sys.setrecursionlimit(10**6)

def dfs(r) :
    global visited
    global dic
    global cnt

    cnt += 1
    visited[r] = cnt
    if r in dic :
        arr = sorted(list(dic[r]))
        for a in arr :
            if visited[a] == 0 :
                dfs(a)

n, m, r = map(int, sys.stdin.readline().split())
dic = {}
visited = [0]*(n+1)

for _ in range(m) :
    u, v = map(int, sys.stdin.readline().split())
    if u in dic :
        dic[u].append(v)
    if v in dic :
        dic[v].append(u)
    if u not in dic :
        dic[u] = [v]
    if v not in dic :
        dic[v] = [u]

cnt = 0
dfs(r)
for i in range(1, n+1) :
    print(visited[i])