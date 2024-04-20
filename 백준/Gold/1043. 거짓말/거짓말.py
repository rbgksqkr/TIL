# --- 요구 사항 ---
# 진실 또는 엄청나게 과장해서 말한다.
# 그 이야기의 진실을 아는 사람들이 파티에 왔을 때는 진실을 이야기할 수 밖에 없다.
# 어떤 사람이 어떤 파티에서는 진실을 듣고, 또다른 파티에서는 과장된 이야기를 들었을 때도 지민이는 거짓말쟁이로 알려지게 된다.
# 지민이는 모든 파티에 참가해야 한다.
# TODO: 지민이가 거짓말쟁이로 알려지지 않으면서, 과장된 이야기를 할 수 있는 파티 개수의 최댓값?
# --- 입력 ---
# 사람의 수 N과 파티의 수 M (N, M은 50 이하의 자연수)
# 이야기의 진실을 아는 사람의 수, 번호
# 각 파티마다 오는 사람의 수, 번호

# --- 풀이 방법 ---
# 파티에 진실을 아는 사람이 오면 False
# truthy[i] 가 true면 false 반환
# 파티마다 새로 truth 배열 갱신
# 이후에 파티에 오는 경우에도 고려해야하기 때문에 같이 오는 파티에서 graph에 저장하여 연결된 상태 저장
# O(n) = 50 * 50 * 50 = 12만5천

import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())

answer = 0
arr = list(map(int, input().split()))

k, knownPeople = arr[0], arr[1:]
visited = [0 for _ in range(n+1)]

graph = [[] for _ in range(n+1)]
parties = []
for _ in range(m):  # 최대 50
    arr = list(map(int, input().split()))
    flag = 0
    count, people = arr[0], arr[1:]
    parties.append(people)
    for i in range(len(people)):  # 최대 50
        for j in range(len(people)):  # 최대 50
            if i == j:
                continue
            graph[people[i]].append(people[j])


def bfs(x):  # m
    queue = deque([x])
    visited[x] = 1
    while queue:
        now = queue.popleft()

        for i in graph[now]:
            if not visited[i]:
                visited[i] = 1
                queue.append(i)


for i in knownPeople:
    bfs(i)
for party in parties:  # m
    flag = 0
    for i in party:
        if visited[i]:
            flag = 1
            break
    if not flag:
        answer += 1
print(answer)
