def find_path(graph, n, start, target):
    dist = [float('inf')] * n
    dist[start] = 0
    visited = [False] * n
    parent = [-1] * n
    
    for _ in range(n):
        u = -1
        for i in range(n):
            if not visited[i] and (u == -1 or dist[i] < dist[u]):
                u = i
        
        if u == -1 or u == target:
            break
            
        visited[u] = True
      
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
    
    if dist[target] == float('inf'):
        return None
    
    path = []
    cur = target
    while cur != -1:
        path.append(cur)
        cur = parent[cur]
    
    return dist[target], path[::-1]

n, m, s, t = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    u, v, d = map(int, input().split())
    graph[u].append((v, d))

res = find_path(graph, n, s, t)
if res:
    print(res[0])
    print(*res[1])
else:
    print("Путь не найден")










    def floyd_warshall(graph):
    n = len(graph)
    dist = [row[:] for row in graph]
    
    for i in range(n):
        for j in range(n):
            if dist[i][j] == -1 and i != j:
                dist[i][j] = float('inf')
            if i == j:
                dist[i][j] = 0
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

n = int(input())
graph = []
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)


result = floyd_warshall(graph)

for row in result:
    print(' '.join(map(str, row)))