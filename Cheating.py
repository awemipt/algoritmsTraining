with open('input.txt') as file:
    V, E = map(int, file.readline().split())
    data = file.read()

Edges = [[] for _ in range(V+1)]
data = data.split('\n')

for i in range(E):
    a, b = map(int, data[i].split())
    Edges[a].append(b)
    Edges[b].append(a)

visited = [0] * (V + 1)
flag = False



def dfs(v, visited, color):
    visited[v] = color
    global flag
    for vertex in Edges[v]:

        if visited[vertex] == color:
            flag = True
        elif visited[vertex] == 0:
            dfs(vertex, visited, 3 - color)

for v in range(1, V+1):
    if visited[v] == 0:
        dfs(v, visited, 1)
if flag:
    print('NO')
else:
    print('YES')