import sys
"""
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
"""

def dfs_stack(r) :
    global dic
    visited = [0]*(n+1)
    cnt = 0
    stack = [r]

    while stack :
        current = stack.pop(-1)

        if visited[current] != 0 :
            continue

        cnt += 1
        visited[current] = cnt

        if current in dic :
            arr = sorted(dic[current], reverse = True)
            for a in arr :
                if visited[a] == 0 :
                    stack.append(a)
    return visited

n, m, r = map(int, sys.stdin.readline().split())
dic = {}
# visited = [0]*(n+1) #-dfs
# cnt = 0 #-dfs

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

#dfs(r)

visited = dfs_stack(r)
for i in range(1, n+1) :
    print(visited[i])