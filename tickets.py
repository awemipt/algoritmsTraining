with open('input.txt') as file:
    N = int(file.readline())
    data = file.read().strip()

A = []
B = []
C = []
for row in data.split('\n'):
    a, b, c = map(int, row.split())
    A.append(a)
    B.append(b)
    C.append(c)
dp = [0] * N
dp[0] = A[0]
if N > 1:
    dp[1] = min(A[1] + A[0], B[0])
if N > 2:
    dp[2] = min(A[2] + A[1]+ A[0], A[2]+ B[0], B[1] + A[0], C[0])
for i in range(3, N):
    dp[i] = min(A[i] + dp[i - 1], B[i - 1] + dp[i - 2], C[i - 2] + dp[i - 3])
print(dp[N-1])
