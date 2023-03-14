with open('input.txt') as file:
    N, M, K = map(int, file.readline().split())
    m = [list(map(int, file.readline().split())) for _ in range(N)]
    requests = [list(map(int, file.readline().split())) for _ in range(K)]

prefix = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        prefix[i][j] = (m[i - 1][j - 1] + prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1])

for x1, y1, x2, y2 in requests:
    print(prefix[x2][y2] - prefix[x1 - 1][y2 ] - prefix[x2 ][y1 - 1] + prefix[x1 - 1][y1 - 1])
