with open('input.txt') as file:
    n = int(file.readline())
    diegos = list(map(int, file.readline().split()))
    collectors = int(file.readline())
    min_values = list(map(int, file.readline().split()))

diegos = set(diegos)
diegos = list(diegos)
diegos.sort()

for collector in min_values:

    l = 0
    r = len(diegos)
    while l != r:
        m = (l + r) // 2
        if diegos[m] >= collector:
            r = m
        else:
            l = m + 1

    print(l)
