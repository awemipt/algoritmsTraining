with open('input.txt') as file:
    string = file.readline().strip()

ans = {k: 0 for k in set(string)}
for i, sym in enumerate(string):
    end = i + 1
    start = len(string) - i
    ans[sym] += end*start

for key in sorted(ans, key=ord, reverse=True):
    print(key,': ', ans[key], sep='')