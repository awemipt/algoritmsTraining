from collections import deque

with open('input.txt') as file:
    N, M, S, T, Q = map(int, file.readline().split())
    flues = []
    for _ in range(Q):
        x, y = map(int, file.readline().split())
        flues.append((x, y))


def is_out_of_pole(i, j):
    if any([i < 0, j < 0, i >= N, j >= M]):
        return True
    return False


marks = [[-1] * M for _ in range(N)]
marks[S-1][T-1] = 0


def bfs(i, j):
    q = deque()
    di = [1, 1, 2, 2, -1, -1, -2, -2]
    dj = [2, -2, 1, -1, 2, -2, 1, -1]
    q.append((i, j ))
    while q:
        i, j = q.popleft()
        for x,y in zip(di, dj):
            if not (is_out_of_pole(i + x, j + y)) and marks[i + x][j + y] == -1:
                marks[i + x][j + y] = 1 + marks[i][j]
                q.append((i+x, j+y))

s = 0
bfs(S-1, T-1)
# for row in marks:
#     print(*row)
for i, j in flues:
    if marks[i-1][j-1] == -1:
        print(-1)
        break
    s += marks[i-1][j-1]
else:
    print(s)