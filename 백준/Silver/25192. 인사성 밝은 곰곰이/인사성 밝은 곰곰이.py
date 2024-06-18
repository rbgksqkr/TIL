import sys
input = sys.stdin.readline
n = int(input())

answer = 0
for _ in range(n):
    line = input().strip()
    if line == 'ENTER':
        visited = {}
    elif visited.get(line):
        visited[line] += 1
    else:
        visited[line] = 1
        answer += 1

print(answer)
