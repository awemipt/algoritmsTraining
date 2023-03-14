from sys import setrecursionlimit
from collections import deque
setrecursionlimit(10 ** 8)
with open('input.txt') as file:
    N = int(file.readline())
    data = file.read().strip()

edges = [[] for _ in range(N + 1)]
i = 1
for row in data.split('\n')[:-1]:
    row = map(int, row.split())
    for j, e in enumerate(row):
        if e == 1:
            edges[i].append(j + 1)
    i += 1

start, end = map(int, data.split('\n')[-1].split())
paths = [[] for _ in range(N + 1)]
distances = [-1] * (N + 1)
distances[start] = 0
distance = [[] for _ in range(N)]
distance[0].append(start)
q = deque()
q.append(start)

while q:
    tmp = q.popleft()
    for v in edges[tmp]:
        if distances[v] == -1:
            distances[v] = distances[tmp] + 1
            q.append(v)
            paths[v] = tmp

print(distances[end])
if distances[end] != -1 and distances[end] != 0:
    tmp = end
    ans = [end]
    while tmp != start:
        tmp = paths[tmp]
        ans.append(tmp)

    print(*reversed(ans))
