# --- 요구사항 ---
# 조카들에게 최대한 긴 과자를 나눠주려고 한다.
# 나눠준 과자의 길이가 하나라도 다르면 조카끼리 싸우므로, 반드시 모든 조카에게 같은 길이의 막대 과자를 나눠주어야 한다.
# TODO: 조카 M명, 과자 N개. 조카 1명에게 줄 수 있는 막대 과자의 최대 길이? 단, 모든 조카에게 같은 길이의 막대과자를 나눠줄 수 없다면, 0 출력.
# M (1 ≤ M ≤ 1,000,000), N (1 ≤ N ≤ 1,000,000), L (1 ≤ L1, L2, ..., LN ≤ 1,000,000,000)

# --- 문제 풀이 ---
# 10억까지 순회하면 시간초과 -> 같은 길이의 최대 길이 결정 -> 이진탐색
# FIXME: 막대 과자는 길이와 상관없이 여러 조각으로 나눠질 수 있지만, 과자를 하나로 합칠 수는 없다. -> 긴 걸 자를 순 있지만 짧은 걸 합칠 수 없음

M, N = map(int, input().split())
snacks = list(map(int, input().split()))

start, end = 1, int(1e9)
answer = 0
while start <= end:
    mid = (start + end) // 2

    count = 0  # mid 길이로 만들 수 있는 과자 개수
    for snack in snacks:
        count += snack // mid

    if count >= M:
        answer = max(answer, mid)
        start = mid + 1
    else:
        end = mid - 1
print(answer)
