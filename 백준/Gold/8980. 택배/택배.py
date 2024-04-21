# --- 요구 사항 ---
# 트럭은 본부에서 출발하여 1번 마을부터 마지막 마을까지 오른쪽으로 가면서 마을에 있는 물건을 배송
# 본부에서는 박스를 보내는 마을번호, 박스를 받는 마을번호와 보낼 박스의 개수를 알고 있다.
# 트럭의 용량이 있다.
# 조건 1: 박스를 트럭에 실으면, 이 박스는 받는 마을에서만 내린다.
# 조건 2: 트럭은 지나온 마을로 되돌아가지 않는다.
# 조건 3: 박스들 중 일부만 배송할 수도 있다.
# 박스를 받는 마을번호는 보내는 마을번호보다 크다.
# TODO: 트럭 한대를 이용하여 조건을 모두 만족하면서 배송할 수 있는 박스의 최대 개수
# --- 풀이 방법 ---
# 다시 되돌아올 수 없으므로 어떤 박스를 트럭에 실을지 결정하는 게 중요
# 보내는 마을번호 순으로 정렬하면 늦게 받을 경우 트럭에 오래 실어야한다.
# 받는 마을번호 순으로 정렬하면 받는 마을번호가 보내는 마을번호보다 크므로 빠르게 트럭을 비워낼 수 있다.
# 근데 해당 마을만 고려하면 (1, 4), (2, 3), (3, 4) 일 때 (1, 4) 박스를 일부 담는 게 손해일 수 있다.
# 전체에서 받는 마을번호 순으로 정렬하고 일부만 담을 박스 결정
# 회의실 배정과 다른 점은 한 타임에 회의를 여러개 할 수 있다.
# --- 힌트 ---
# 각 마을에서 실을 수 있는 만큼 빼기
# 출발지-도착지 사이 마을의 트럭 용량에서 박스 개수만큼을 뺀다. (박스개수가 트럭용량보다 작을경우 트럭용량을 뺀다)

# 입력
# 마을 개수 : N (2이상 2,000이하 정수)
# 트럭 용량 : C (1이상 10,000이하 정수)
# 보내는 박스 정보의 개수 : M (1이상 10,000이하 정수)
# 보내는 박스 개수 (1이상 10,000이하 정수)

import sys
input = sys.stdin.readline

n, c = map(int, input().split())
m = int(input())
graph = []
for _ in range(m):
    sender, receiver, boxCount = map(int, input().split())
    graph.append([sender, receiver, boxCount])
graph.sort(key=lambda x: x[1])

answer = 0
containers = [c for _ in range(n+1)]  # 실을 수 있는 만큼 빼기

for delivery in graph:
    start, end, boxCount = delivery
    minBoxCount = c

    for i in range(start, end):
        if minBoxCount > min(containers[i], boxCount):
            minBoxCount = min(containers[i], boxCount)

    for i in range(start, end):
        containers[i] -= minBoxCount
    answer += minBoxCount
print(answer)
