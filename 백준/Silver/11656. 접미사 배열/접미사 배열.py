import sys
input = sys.stdin.readline

data = input().strip()
arr = []
for i in range(len(data)):
    arr.append(data[i:])
arr.sort()
for i in arr:
    print(i)
