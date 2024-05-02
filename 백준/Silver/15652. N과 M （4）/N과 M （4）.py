# --- 요구 사항 ---
# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
# 고른 수열은 비내림차순이어야 한다.
# 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

# TODO: 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하기
# --- 풀이 방법 ---
# 나의 인덱스를 넘기고 해당 인덱스부터 반복문 돌기

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

answer = []


def dfs(x):
    if len(answer) == m:
        print(*answer)
        return

    for i in range(x, n+1):
        answer.append(i)
        dfs(i)
        answer.pop()


dfs(1)
