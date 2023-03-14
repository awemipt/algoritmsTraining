labirint = []
with open('input.txt') as file:
    N, M = map(int, file.readline().split())
    for _ in range(N):
        labirint.append(file.readline())
    start_x, start_y = map(int, file.readline().split())
    end_x, end_y = map(int, file.readline().split())
start_x, start_y = start_x - 1, start_y - 1
end_x, end_y = end_x - 1, end_y - 1
start_y = N - start_y - 1
end_y = N - 1 - end_y
dist = [[-1] * M for _ in range(N)]
dist[start_y][start_x] = 0
dx = [1, 1, 1, 0, 0, -1, -1, -1]
dy = [1, 0, -1, 1, -1, 1, 0, -1]
from collections import deque

q = deque()
q.append((start_y, start_x, -10, -10))
# print(start_x, start_y)


def is_out_pole(i, j):
    if any([i < 0, j < 0, i >= N, j >= M]):
        return True
    return False


while q:
    i, j, prev_y, prev_x = q.popleft()
    for x, y in zip(dx, dy):
        if not (is_out_pole(i + y, j + x)) and labirint[i + y][j + x] == '.' and (dist[i + y][j + x] == -1):
            # print(prev_x, j, x)
            # print(prev_y, i, y)
            if j - prev_x == x and i - prev_y == y:

                dist[i + y][j + x] = dist[i][j]
            else:
                dist[i + y][j + x] = dist[i][j] + 1
            q.append((i + y, j + x, i, j))
    # print(q)
for row in dist:
    print(*row)

print(dist[end_y][end_x])