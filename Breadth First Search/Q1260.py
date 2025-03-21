from collections import deque

def dfs(graph, v, visited) :
    visited[v] = True
    print(v, end=' ')
    for i in graph[v] :
        if not visited[i] :
            dfs(graph, i, visited)

def bfs(graph, v, visited) :
    queue = deque([v])
    visited[v] = True

    while queue :
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True

n, m, v = map(int,input().split())
g = {i: [] for i in range(n+1)} #0~
visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)
for _ in range(m) :
    node1, node2 = map(int, input().split())
    g[node1].append(node2)
    g[node2].append(node1)
for i in g :
    g[i] = sorted(g[i])

dfs(g, v, visited_dfs)
print()
bfs(g, v, visited_bfs)