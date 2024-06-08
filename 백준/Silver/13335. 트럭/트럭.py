# --- 요구사항 ---
# n 개의 트럭
# 트럭의 순서는 바꿀 수 없으며, 트럭의 무게는 서로 같지 않을 수 있다.
# 다리 위에는 단지 w 대의 트럭만 동시에 올라갈 수 있다.
# 다리의 길이는 w 단위길이(unit distance)
# 각 트럭들은 하나의 단위시간(unit time)에 하나의 단위길이만큼만 이동
# 동시에 다리 위에 올라가 있는 트럭들의 무게의 합은 다리의 최대하중인 L보다 작거나 같아야 한다.

# --- 풀이방법 ---
# 1. 다리를 배열로 저장해서 돌리기
# 2. 트럭이 다리에 올라갈 수 있을지 결정하기


import sys
from collections import deque
input = sys.stdin.readline

n, w, l = map(int, input().split())
trucks = list(map(int, input().split()))

trucks = deque(trucks)
bridges = deque([0 for _ in range(w)])
count = 0
while bridges:
    count += 1  # 시간 1 증가
    bridges.popleft()

    if trucks:  # 건널 트럭이 있을 때
        if trucks[0] + sum(bridges) <= l:  # 맨앞차례 트럭 무게 + 다리 위에 트럭 무게가 l 이하일 때
            bridges.append(trucks.popleft())  # 다리 위에 추가
        else:  # 다리 위에 있는 트럭만 전진
            bridges.append(0)

print(count)
