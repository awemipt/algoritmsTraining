with open('input.txt') as file:
    N = int(file.readline())
    K = int(file.readline())
    row = int(file.readline())
    place = int(file.readline())
flag = True
place1 = place + 2 * (row- 1)
place2M = place1 + K
place2m = place1 - K
rows = (N + 1) // 2
row1 = (place2M +1) //2
row2 = (place2m + 1) // 2

if place2M > N and place2m <= 0:
    print(-1)
else:
    if row2 - row <= row - row1 and place2M <=N:
        print((place2M+1) // 2 , 2 if place2M % 2 == 0 else 1)
    else:
        print((place2m+1) // 2 , 2 if place2m % 2 == 0 else 1)
