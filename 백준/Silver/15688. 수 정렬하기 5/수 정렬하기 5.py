import sys
input = sys.stdin.readline

n = int(input())

arr = []
count = [0 for _ in range(2000001)]
for _ in range(n):
    arr.append(int(input()))

for i in arr:
    count[i+1000000] += 1

for idx, i in enumerate(count):
    if i > 0:
        for j in range(i):
            print(idx-1000000)
