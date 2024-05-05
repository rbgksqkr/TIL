import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

answer = []


def dfs(x):

    if len(answer) == m:
        print(*answer)
        return

    for i in range(x, n):
        if data[i] not in answer:
            answer.append(data[i])
            dfs(i+1)
            answer.pop()


dfs(0)
