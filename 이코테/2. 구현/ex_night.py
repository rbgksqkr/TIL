n = input()
row = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
x, y = int(n[1])-1, row[n[0]]
move = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

result = 0
for i in range(8):
    dx = x + move[i][0]
    dy = y + move[i][1]

    if dx < 0 or dy < 0 or dx >= 8 or dy >= 8:
        continue
    
    result += 1

print(result)