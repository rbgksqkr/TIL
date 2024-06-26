# --- 요구 사항 ---
# N개의 수 중에서 '어떤 수' === '서로 다른 두 수의 합' : 좋다(GOOD)
# 수의 위치가 다르면 값이 같아도 다른 수.
# TODO: N개의 수가 주어지면 그 중에서 좋은 수의 개수는 몇 개?

# --- 풀이 방법 ---
# 어떤 수를 골라야 한다 -> N
# 1번을 선택 -> N
# 1번과 더할 2번을 골라서 어떤 수가 되는지 확인 -> N => N^3 (X)
# 1번은 순회하고(고정), 2번을 이분탐색으로 선택 : N^2 *logN
# 67% 틀렸습니다.

import sys
input = sys.stdin.readline
N = int(input())
targets = list(map(int, input().split()))
targets.sort()

count = 0
for i in range(N):
    temp = targets[:i] + targets[i+1:]
    start, end = 0, len(temp)-1

    while start < end:
        total = temp[start] + temp[end]

        if total == targets[i]:
            count += 1
            break

        elif total < targets[i]:
            start += 1

        elif total > targets[i]:
            end -= 1

print(count)
