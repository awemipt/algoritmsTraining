A = []
T = []
with open('input.txt') as file:
    N, W = map(int,file.readline().split())
    for _ in range(N):
        a, t = map(int, file.readline().split())
        A.append(a)
        T.append(t)


