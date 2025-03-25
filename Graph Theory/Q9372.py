def dfs(graph, v, visited, cnt) :
    visited[v] = 1
    for i in graph[v] :
        if not visited[i] :
            cnt = dfs(graph, i, visited, cnt+1)
    return cnt

t = int(input())

for _ in range(t) :
    n, m = map(int, input().split())
    visited = [0] * (n+1)
    visited[0] = 1
    dic = { d : [] for d in range(1, n+1)}
    for _ in range(m) :
        a, b = map(int, input().split())
        dic[a].append(b)
        dic[b].append(a)
    cnt = dfs(dic, 1, visited, 0)
    print(cnt)




