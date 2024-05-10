# --- 요구 사항 ---
# 수열 A = {10, 20, 10, 30, 20, 50} 인 경우,
# 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.
# TODO: 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열?

# --- 풀이 방법 ---
# dp[i][j] : j번째까지 i보다 큰 값의 개수
# O(N^2)으로 풀면 시간초과
# dp + 이분탐색으로 O(NlogN)

import sys
input = sys.stdin.readline
n = int(input())
graph = list(map(int, input().split()))

dp = []
dp.append(graph[0])


def binarySearch(e):
    start = 0
    end = len(dp) - 1

    while start <= end:
        mid = (start + end) // 2

        if dp[mid] == e:
            return mid
        elif dp[mid] < e:
            start = mid + 1
        else:
            end = mid - 1

    return start


for i in range(n):
    if graph[i] > dp[-1]:
        dp.append(graph[i])
    else:
        idx = binarySearch(graph[i])
        dp[idx] = graph[i]

print(len(dp))
