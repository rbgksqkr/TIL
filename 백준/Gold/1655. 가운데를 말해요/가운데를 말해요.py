# --- 문제 분석 ---
# 정수를 외칠 때마다, 지금까지 말한 수 중에서 중간값 출력
# 지금까지 말한 수가 짝수개라면, 중간에 있는 두 수 중 작은 수 출력

# 예를 들어 백준이가 동생에게 1, 5, 2, 10, -99, 7, 5를 순서대로 외쳤다고 하면,
# 동생은 1, 1, 2, 2, 2, 2, 5를 차례대로 말해야 한다.

# TODO: 백준이가 외치는 수가 주어졌을 때, 동생이 말해야 하는 수 출력

# --- 풀이 방법 ---
# N (1 <= N <= 100000)
# 정수 (-10,000 <= 정수 <= 10,000)
# 0.1초 -> O(N) 1000만 이하
# 매번 정렬 시 N^2 logN 으로 초과
# 최소힙으로 push할 때 오름차순으로 정렬되기 한 다음 중간값 계산
# 근데 heap은 중간 인덱스가 중간값이 아님
# FIXME: heap을 중간값을 기준으로 leftHeap, rightHeap으로 나눔
# FIXME: leftHeap은 중간값보다 작은 최대힙, rightHeap은 중간값보다 큰 최소힙.
# 짝수개일 때 작은 수가 중간값이므로, leftHeap의 root가 중간값이 되어야함.
# leftHeap의 루트보다 rightHeap의 루트가 작을 경우 교체

import heapq
import sys

input = sys.stdin.readline
n = int(input())

leftHeap, rightHeap = [], []
answer = []

for _ in range(n):
    num = int(input())

    if len(leftHeap) == len(rightHeap):
        # 최대힙을 위해 정렬 기준인 마이너스 붙인 값을 1번째 인자, 실제 값을 2번째 인자로
        heapq.heappush(leftHeap, [-num, num])
    else:
        heapq.heappush(rightHeap, [num, num])

    # leftHeap의 최대보다 rightHeap의 최소가 작을 경우 교체
    if rightHeap and leftHeap[0][1] > rightHeap[0][1]:
        leftValue = heapq.heappop(leftHeap)[1]
        rightValue = heapq.heappop(rightHeap)[1]

        heapq.heappush(leftHeap, [-rightValue, rightValue])
        heapq.heappush(rightHeap, [leftValue, leftValue])

    answer.append(leftHeap[0][1])

for i in answer:
    print(i)
