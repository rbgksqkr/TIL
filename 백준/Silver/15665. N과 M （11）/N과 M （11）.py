import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

result = []
answer = []


def dfs():
    if len(result) == m:
        temp = []
        for i in result:
            temp.append(data[i])
        answer.append(temp)
        return

    for i in range(n):
        result.append(i)
        dfs()
        result.pop()


dfs()
unique_list = list(set(map(tuple, answer)))
unique_list.sort()

for i in unique_list:
    print(*i)
