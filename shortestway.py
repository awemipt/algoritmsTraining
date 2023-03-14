from sys import setrecursionlimit

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
distances = [-1] * (N+1)
distances[start] = 0
distance = [[] for _ in range(N)]
distance[0].append(start)
for i in range(0,N):
    for vertex in distance[i]:
        for next_vertex in edges[vertex]:
            if distances[next_vertex] == -1:
                distances[next_vertex] = distances[vertex] +1
                distance[i+1].append(next_vertex)
print(distances[end])


