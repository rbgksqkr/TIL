from collections import deque

def rotateLeft(idx, dir):
    if idx < 0 or gears[idx][2] == gears[idx+1][6]:
        return
    
    if gears[idx][2] != gears[idx+1][6]:
        rotateLeft(idx-1, -dir)
        gears[idx].rotate(dir)

def rotateRight(idx, dir):
    if idx > 3 or gears[idx][6] == gears[idx-1][2]:
        return
    
    if gears[idx][6] != gears[idx-1][2]:
        rotateRight(idx+1, -dir)
        gears[idx].rotate(dir)

gears = []
for _ in range(4):
    gears.append(deque(list(input().strip())))
k = int(input())
rotates = []
for _ in range(k):
    a, b = map(int, input().split()) # [회전시킨 톱니바퀴의 번호, 방향]. 방향 : 1 시계, -1 반시계
    rotates.append([a-1, b])

for i in rotates:
    number, dir = i
    rotateLeft(number-1, -dir)
    rotateRight(number+1, -dir)
    gears[number].rotate(dir) # deque.rotate() : 1 시계, -1 반시계

answer = 0
for i in range(4):
    if gears[i][0] == '1':
        answer += 2**i
print(answer)
