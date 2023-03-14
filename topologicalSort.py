from sys import setrecursionlimit
setrecursionlimit(10**8)
with open('input.txt') as file:
    V, E = map(int, file.readline().split())
    data = file.read().strip()

edges = [[] for _ in range(V + 1)]
for row in data.split('\n'):
    a, b = map(int, row.split())
    edges[a].append(b)

ans = []
visited = [0] * (V + 1)
flag = False


def dfs(vertex):
    global flag, visited, ans
    visited[vertex] = 1
    for v in edges[vertex]:
        if visited[v] == 1:
            flag = True
        elif visited[v] == 0:
            dfs(v)
    visited[vertex] = 2
    ans.append(vertex)


for v in range(1, V + 1):
    if visited[v] == 0:
        dfs(v)

if flag:
    print(-1)
else:
    print(*reversed(ans))
