from sys import setrecursionlimit
setrecursionlimit(10**8)
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
connect = [0] * (V)
def dfs(edges, visited, vertex, connected):
    visited[vertex] = True
    connect[vertex-1] = connected
    connected_vertex[connected-1].append(vertex)
    for v in edges[vertex]:
        if not visited[v]:
            dfs(edges, visited, v, connected)


con = 1
connected_vertex =[]
for i in range(1,V+1):
    if not visited[i]:
        connected_vertex.append([])
        dfs(Edges, visited, i, con)
        con += 1

print(len(set(connect)))

for c in set(connect):

    print(len(connected_vertex[c-1]))
    print(*connected_vertex[c-1])
