import sys
from collections import deque

def infact_d(g, v, visited) : #dfs
    visited[v] = 1
    for i in g[v] :
        if visited[i] == 0 :
            infact_d(g, i, visited)

def infact_b(g, visited) : #bfs
    visited[1] = 1
    q = deque([1])

    while q :
        v = q.popleft()
        for i in g[v] :
            if visited[i] == 0 :
                q.append(i)
                visited[i] = 1

n = int(sys.stdin.readline())
p = int(sys.stdin.readline())

graph = {
    i : [] for i in range(n+1)
}
for _ in range(p) :
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n+1)
#infact_d(graph, 1, visited)
infact_b(graph, visited)
print(visited.count(1)-1)