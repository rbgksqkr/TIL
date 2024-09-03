# --- 문제 분석 ---
# 수열에서 같은 원소가 여러 개 들어 있는 수열을 싫어한다.
# 같은 원소가 K개 이하로 들어 있는 최장 연속 부분 수열의 길이를 구하려고 한다.

# 100000 이하의 양의 정수로 이뤄진 길이가 N인 수열이 주어진다.
# TODO: 이 수열에서 같은 정수를 K개 이하로 포함한 "최장 연속 부분 수열의 길이" 출력

# --- 문제 풀이 ---
# 1. n, k 입력받는다.
# 2. 수열을 공백 기준으로 입력받는다.
# 3. k번 이하 횟수만큼 수열에 포함하려면 해당 원소가 몇번 나왔는지 기억해야한다. -> dp 테이블에 저장
# 4. dp[i][j] = i번째 인덱스부터 시작해서 j
# FIXME: 배열에 몇번 나왔는지 카운팅하고 범위를 투포인터로 지정

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

start, end = 0, 0
numbers = [0 for _ in range(max(arr)+1)]
answer = 0

while end < n:  # end가 n과 같아지면 break
    if numbers[arr[end]] >= k:
        numbers[arr[start]] -= 1
        start += 1
    else:
        numbers[arr[end]] += 1
        end += 1
        answer = max(answer, end - start)

print(answer)
