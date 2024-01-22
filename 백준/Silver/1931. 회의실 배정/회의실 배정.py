import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    start, end = map(int, input().split())
    arr.append([start, end])
arr.sort(key=lambda x: (x[1], x[0]))

answer = 1
start, end = arr[0]
for i in range(1, n):
    if end <= arr[i][0]:
        end = arr[i][1]
        answer += 1
print(answer)
