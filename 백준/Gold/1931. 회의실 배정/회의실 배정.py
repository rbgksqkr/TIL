import sys
input = sys.stdin.readline

n = int(input())
confs = []
for _ in range(n):
	start, end = map(int, input().split())
	confs.append([start, end])

confs.sort(key=lambda x:(x[1], x[0]))

last = 0
count = 0
for conf in confs:
    start, end = conf
    if start >= last:
        count += 1
        last = end

print(count)