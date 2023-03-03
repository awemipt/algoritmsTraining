with open('input.txt') as file:
    n = int(file.readline())
    diegos = list(map(int, file.readline().split()))
    collectors = int(file.readline())
    min_values = list(map(int, file.readline().split()))

diegos = set(diegos)
ans = {}
for collector in min_values:
    tmp = 0
    if collector not in ans:
        for mark in diegos:
            if mark < collector:
                tmp += 1
        ans[collector] = tmp
    tmp = ans[collector]
    print(tmp)
