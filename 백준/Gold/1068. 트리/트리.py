# 노드를 지우면 그 노드와 노드의 모든 자손이 트리에서 제거
# TODO: 각 노드의 부모 노드를 입력값으로 줬을 때 자식 노드 개수 세기

# 자식 노드를 다 지우고, 부모도 지워
# 리프노드인지 어떻게 판단? -> 배열로 따로 관리?
# tree에서 빈배열이면 리프노드

import sys
input = sys.stdin.readline

n = int(input())

# 1. tree 구조로 데이터 저장하기
tree = [[] for _ in range(n)]
visited = [False] * n
root = answer = 0

inputData = list(map(int, input().split()))

for node, parent in enumerate(inputData):
    if parent == -1:
        root = node
    else:
        tree[parent].append(node)

# 2. target 노드 하위 노드 모두 제거하기 -> 실제로 제거하지 않고 방문처리해놓고 하위 노드 탐색 안하기
target = int(input())
visited[target] = True


def dfs(s):
    global answer

    if visited[s]:
        return
    visited[s] = True

    if len(tree[s]) == 0:
        answer += 1
        return
    elif len(tree[s]) == 1 and tree[s][0] == target:
        answer += 1

    for x in tree[s]:
        dfs(x)


# 3. DFS로 리프 노드 개수 세기
dfs(root)
print(answer)
