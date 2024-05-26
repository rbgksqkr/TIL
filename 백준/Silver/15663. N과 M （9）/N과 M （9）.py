import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

answer = []
result = []


def dfs():
    if len(answer) == m:

        temp = []
        for i in answer:
            temp.append(data[i])
        result.append(temp)
        return

    for i in range(len(data)):
        if i not in answer:
            answer.append(i)
            dfs()
            answer.pop()


dfs()

unique_list = list(set(map(tuple, result)))
total = list(map(list, unique_list))
total.sort()

for i in total:
    print(*i)
