with open('input.txt') as file:
    n = int(file.readline())
    data = file.read()
mx = my = Mx = My = None
data = data.strip()
for line in data.split('\n'):
    x, y = map(int, line.split())
    if mx is None or x < mx:
        mx = x
    if Mx is None or x > Mx:
        Mx = x
    if my is None or y < my:
        my = y
    if My is None or y > My:
        My = y

print(mx, my, Mx, My)