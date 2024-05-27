import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

result = []
answer = []


def dfs(x):
    if len(result) == m:
        temp = []
        for i in result:
            temp.append(data[i])
        answer.append(temp)
        return
    for i in range(x, n):
        if i not in result:
            result.append(i)
            dfs(i + 1)
            result.pop()


dfs(0)
unique_list = list(map(list, set(map(tuple, answer))))
unique_list.sort()
for i in unique_list:
    print(*i)
