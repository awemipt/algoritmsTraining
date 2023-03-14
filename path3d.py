from collections import deque

d3 = []
with open('input.txt') as file:
    N = int(file.readline())

    for _ in range(N):
        file.readline()
        tmp = []
        for __ in range(N):
            tmp.append(file.readline().strip())
        d3.append(tmp)


i = 0
j = 0
k = 0
si, sj, sk = None, None, None
for layer in d3:
    j = 0
    for line in layer:
        k = 0
        for sym in line:
            if sym == 'S':
                si, sj, sk = i, j, k
            k += 1
        j += 1
    i += 1


def is_out(i, j, k):
    if any([i < 0, j < 0, k < 0, i >= N, j >= N, k >= N]):
        return True
    return False


paths = [[[-1] * N for _ in range(N)] for __ in range(N)]

paths[si][sj][sk] = 0
q = deque()
q.append((si, sj, sk))
di = [-1, 1, 0, 0, 0, 0]
dj = [ 0, 0, -1, 1, 0, 0]
dk = [ 0, 0, 0 , 0, -1, 1]
while q:
    i, j , k = q.popleft()
    for x, y, z in zip(di, dj, dk):
        if not(is_out(i+x,j+y,k + z)) and paths[i+x][j+y][k+z] == -1 and d3[i+x][j+y][k+z] =='.':
            paths[i + x][j + y][k + z] = paths[i][j][k] + 1
            q.append((i+x,j+y,k+z))
ans = None
for row in paths[0]:
    for num in row:
        if num != -1 and (ans is None or num < ans):
            ans = num
print(ans)
