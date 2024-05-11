import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
answer = []


def dfs():
    global answer
    if len(answer) == m:
        print(*answer)
        return

    for i in range(n):
        answer.append(data[i])
        dfs()
        answer.pop()


dfs()
