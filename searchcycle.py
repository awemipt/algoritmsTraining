from sys import setrecursionlimit

setrecursionlimit(10 ** 8)
with open('input.txt') as file:
    N = int(file.readline())
    data = file.read()

edges = [[] for _ in range(N + 1)]
i = 1
for row in data.split('\n'):
    row = map(int, row.split())
    for j, e in enumerate(row):
        if e == 1:
            edges[i].append(j + 1)
    i += 1

visited = [0] * (N + 1)

flag = False

ans = []


# for row in edges:
#     print(row)
tmpans = []
def dfs(prev, v):
    global visited, edges, flag, ans, tmpans
    visited[v] = 1
    tmpans.append(v)
    for e in edges[v]:
        if not flag and e != prev and visited[e] == 1:
            flag = True

            ans = tmpans[tmpans.index(e):][:]
            # flag = True
            # start = e
            # prev2 = start
            # end = v
            # ans.append(end)
            #
            # while end != start:
            #     for tmp in edges[end]:
            #         if visited[tmp] == 1 and tmp != prev2:
            #             ans.append(tmp)
            #             prev2 = end
            #             end = tmp
            #             break

        elif visited[e] == 0:
            dfs(v, e)
    tmpans.remove(v)
    visited[v] = 2


for i in range(1, N + 1):
    if visited[i] == 0:
        dfs(0, i)
if flag:
    print('YES')
    print(len(ans))
    print(*ans)
else:
    print('NO')
