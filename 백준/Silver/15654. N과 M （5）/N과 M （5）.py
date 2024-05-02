# --- 요구 사항 ---
# N개의 자연수 중에서 M개를 고른 수열
# TODO: N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열 모두 구하기
# --- 풀이 방법 ---
# 1 7 이랑 7 1 을 다르다고 판단
# 사전 순으로 증가하는 순서로 출력
# --- 입력 ---
# 4 2
# 9 8 7 1
# --- 출력 ---
# 1 7
# 1 8
# 1 9
# 7 1
# ...
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

answer = []


def dfs():
    if len(answer) == m:
        print(*answer)
        return

    for i in range(n):
        if data[i] not in answer:
            answer.append(data[i])
            dfs()
            answer.pop()


dfs()
