import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
answer = []


def dfs(x):
    global answer
    if len(answer) == m:
        print(*answer)
        return

    for i in range(n):
        if x > data[i]:
            continue
        answer.append(data[i])
        dfs(data[i])
        answer.pop()


dfs(0)
