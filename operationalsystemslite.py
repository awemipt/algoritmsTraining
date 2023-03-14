with open('input.txt') as file:
    M = int(file.readline())
    N = int(file.readline())

    opers = [tuple([x for x in list(map(int, file.readline().split()))]) for _ in range(N)]

writed = []

for a, b in opers:

    tmp_writed = []
    for x in writed:
        c, d = x
        if not(a <= d and c <= b):
            tmp_writed.append(x)
    writed = tmp_writed
    writed.append((a, b))
# print(writed)
print(len(writed))
