from collections import deque

with open('input.txt') as file:
    N = int(file.readline())
    M = int(file.readline())
    lines = []
    for line in range(M):
        lines.append(list(map(int, file.readline().split()))[1:])
    start, end = map(int, file.readline().split())
V = M
links = [[] for _ in range(M)]
for i in range(M):
    for j in range(M):
        if i != j and set(lines[i]) & set(lines[j]):
            links[i].append(j)
dist = [-1] * V
# print(links)
q = deque()
for i, line in enumerate(lines):
    if start in set(line):
        dist[i] = 0
        q.append(i)
# print(q)
while q:
    tmp = q.popleft()
    for line in links[tmp]:
        if dist[line] == -1:
            dist[line] = dist[tmp] + 1
            q.append(line)
m = None
# print(dist)
for i, line in enumerate(lines):
    if end in set(line):
        if m is None or dist[i] < m:
            m = dist[i]
print(m)
