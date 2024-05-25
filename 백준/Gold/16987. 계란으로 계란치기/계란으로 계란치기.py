# 계란으로 계란을 치게 되면 각 계란의 내구도는 상대 계란의 무게만큼 깎이게 된다.
# 그리고 내구도가 0 이하가 되는 순간 계란은 깨지게 된다.
# 예를 들어 계란 1의 내구도가 7, 무게가 5이고 계란 2의 내구도가 3, 무게가 4라고 해보자.
# 계란 1으로 계란 2를 치게 되면 계란 1의 내구도는 4만큼 감소해 3이 되고 계란 2의 내구도는 5만큼 감소해 -2가 된다.
# 충돌 결과 계란 1은 아직 깨지지 않았고 계란 2는 깨졌다.
# 왼쪽부터 차례로 들어서 한 번씩만 다른 계란을 쳐 최대한 많은 계란을 깨는 문제
# TODO: 일렬로 놓인 계란들의 내구도와 무게가 차례대로 주어졌을 때 최대 몇 개의 계란을 깰 수 있는가?

import sys
input = sys.stdin.readline
n = int(input())
graph = []
for _ in range(n):
    s, w = map(int, input().split())
    graph.append([s, w])


def dfs(x):
    global answer

    if x == n:  # 끝에 오는 경우
        total = 0
        for i in graph:
            if i[0] <= 0:
                total += 1
        answer = max(answer, total)
        return

    if graph[x][0] <= 0:  # 손에 들고 있는 계란이 깨진 경우
        dfs(x+1)
        return

    isAllCrushed = True
    for i in range(n):
        if i == x:
            continue
        if graph[i][0] > 0:
            isAllCrushed = False
            break

    if isAllCrushed:  # 손에 들고 있는 계란 빼고 다 깨져있는 경우
        answer = max(answer, n-1)
        return

    for i in range(n):
        if i == x or graph[i][0] <= 0:
            continue
        graph[x][0] -= graph[i][1]
        graph[i][0] -= graph[x][1]
        dfs(x+1)
        graph[x][0] += graph[i][1]
        graph[i][0] += graph[x][1]


answer = 0
dfs(0)
print(answer)
