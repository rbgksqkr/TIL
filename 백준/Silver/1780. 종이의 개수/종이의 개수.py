# --- 요구 사항 ---
# NxN. # 종이에는 -1, 0, 1 저장.
# 1. 종이가 모두 같은 수면 종이 사용
# 2. (1) 에 해당되지 않는다면 같은 크기의 종이 9개로 자르고, 잘린 종이에 대해 1번 과정 반복
# TODO: -1로만 채워진 종이의 개수, 0으로만 채워진 종이의 개수, 1로만 채워진 종이의 개수

# --- 문제 풀이 ---
# [0, 0]부터 순회.
# board[0][0] 과 다른 값을 만나면 자른다 -> 범위를 좁힌다
# -1, 0, 1 개수를 각각 저장 후 출력

import sys
input = sys.stdin.readline

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
minusCount, zeroCount, plusCount = 0, 0, 0


def check(row, col, n):
    global minusCount, zeroCount, plusCount
    curr = board[row][col]

    for i in range(row, row + n):
        for j in range(col, col + n):
            if board[i][j] != curr:
                next_n = n // 3
                check(row, col, next_n)  # 1
                check(row, col + next_n, next_n)  # 2
                check(row, col + (2 * next_n), next_n)  # 3
                check(row + next_n, col, next_n)  # 4
                check(row + next_n, col + next_n, next_n)  # 5
                check(row + next_n, col + (2 * next_n), next_n)  # 6
                check(row + (2 * next_n), col, next_n)  # 7
                check(row + (2 * next_n), col + next_n, next_n)  # 8
                check(row + (2 * next_n), col + (2 * next_n), next_n)  # 9
                return

    if curr == -1:
        minusCount += 1
    elif curr == 0:
        zeroCount += 1
    elif curr == 1:
        plusCount += 1


check(0, 0, N)

print(minusCount)
print(zeroCount)
print(plusCount)
