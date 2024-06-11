import sys
input = sys.stdin.readline

data = []
max_length = 0
for _ in range(5):
    line = input().strip()
    max_length = max(max_length, len(line))
    data.append(list(line))

for i in range(5):
    if len(data[i]) < max_length:
        data[i] += [-1 for _ in range(max_length - len(data[i]))]

for i in range(max_length):
    for j in range(5):
        if data[j][i] == -1:
            continue
        print(data[j][i], end='')
