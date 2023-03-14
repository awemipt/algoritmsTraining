with open('input.txt') as file:
    V, E = map(int, file.readline().split())
    data = file.read().strip()
Edges = [set() for _ in range(V + 1)]
data = data.split('\n')
for e in range(E):
    v1, v2 = map(int, data[e].split())
    Edges[v1].add(v2)
    Edges[v2].add(v1)


visited = [False] * (V + 1)
def dfs(edges, visited, vertex):
    visited[vertex] = True
    for v in edges[vertex]:
        if not visited[v]:
            dfs(edges, visited, v)

dfs(Edges, visited, 1)
print(sum(visited))
for i in range(V+1):
    if visited[i]:
        print(i, end=' ')