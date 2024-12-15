# 노드를 지우면 그 노드와 노드의 모든 자손이 트리에서 제거
# TODO: 각 노드의 부모 노드를 입력값으로 줬을 때 자식 노드 개수 세기

# 자식 노드를 다 지우고, 부모도 지워
# 리프노드인지 어떻게 판단? -> 배열로 따로 관리?
# tree에서 빈배열이면 리프노드

import sys
input = sys.stdin.readline

n = int(input())
# inputData = map(int, input().split())
# target = int(input())

# tree = {}

# for i in range(n):
#     tree[i] = []

# for idx, data in enumerate(inputData):
#     # -1 이면 만들고 빈 배열
#     # -1 아닌데 없으면 만들고 추가
#     # 있으면 추가
#     if not tree.get(data):
#         if data != -1:
#             tree[data] = [idx]
#     else:
#         tree[data].append(idx)

# # target 노드 하위로 제거하기


# def deleteTree(root):
#     for i in tree[root]:
#         if tree[i]:
#             deleteTree(i)
#         del tree[i]


# deleteTree(target)
# del tree[target]

# # # 리프 노드 개수 세기
# answer = 0
# for v in tree.values():
#     if len(v) == 0:
#         answer += 1
# print(answer)

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
