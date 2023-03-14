from collections import deque

with open('input.txt') as file:
    player1 = list(map(int, file.readline().split()))
    player2 = list(map(int, file.readline().split()))

player1 = deque(player1)
player2 = deque(player2)
turn = 0

while player1 and player2:
    c1 = player1.popleft()
    c2 = player2.popleft()
    # print(turn, c1, c2)
    if c1 == 0 and c2 == 9:
        player1.append(c1)
        player1.append(c2)
    elif c2 == 0 and c1 == 9:
        player2.append(c1)
        player2.append(c2)
    elif c1 > c2:
        player1.append(c1)
        player1.append(c2)
    else:
        player2.append(c1)
        player2.append(c2)

   
    turn += 1
    if turn > 10**6:
        print('botva')
        break
else:
    if player1:
        print('first', turn)
    else:
        print('second', turn)