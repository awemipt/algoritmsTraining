with open('input.txt') as file:
    n = int(file.readline())
    acids = list(map(int, file.readline().split()))
flag = False
for i in range(len(acids)-1):
    if acids[i] > acids[i+1]:
        flag = True

if flag:
    print(-1)
else:
    print(acids[-1]-acids[0])