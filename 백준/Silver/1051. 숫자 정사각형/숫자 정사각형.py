import sys
input = sys.stdin.readline

n, m = map(int, input().split())

data = []
for _ in range(n):
    data.append(list(map(int, list(input().strip()))))

max_area = 1
for i in range(n):
    for j in range(m):
        number = data[i][j]
        k = 1
        while i+k < n and j+k < m:
            if number == data[i][j+k] and number == data[i+k][j] and number == data[i+k][j+k]:
                max_area = max(max_area, pow(k+1, 2))
            k += 1

print(max_area)