from string import ascii_lowercase
with open('input.txt') as file:
    k = int(file.readline())
    string = file.readline()

ans = 0
for sym in ascii_lowercase:
    l = r = 0
    tmpk = k
    for step in string:
        while tmpk >= 0 and r < len(string):
            p = string[r]
            if string[r] != sym:
                tmpk -= 1
            if tmpk != -1:
                r += 1
            # r += 1
        if tmpk == -1:
            tmpk = 0
        ans = max( r - l, ans)
        if r == len(string):
            break
        if string[l] != sym:
            tmpk += 1
        l += 1
    if ans == len(string):
        break
print(ans)