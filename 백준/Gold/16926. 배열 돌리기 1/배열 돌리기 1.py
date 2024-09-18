# --- 문제 분석 ---
# N×m인 배열을 반시계 방향으로 회전

# --- 문제 풀이 ---
# 1. n, m, r 입력 받기. nxm 배열. r번 반시계 회전.
# FIXME: 각 껍질별로 1차원으로 나열하는 것이 후에 회전 작업

import sys
from collections import deque
input = sys.stdin.readline
n, m, r = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
answer = [[0]*m for _ in range(n)]

queue = deque()
for i in range(min(n, m) // 2):
    # 2차원 배열을 1차원 배열로 만들기
    queue.clear()
    queue.extend(board[i][i:m-i])  # 위쪽. board[0][0~m-1] / board[1][1~m-2]
    queue.extend([row[m-i-1] for row in board[i+1:n-i-1]]) 	# 오른쪽
    queue.extend(board[n-i-1][i:m-i][::-1]) 		# 아래쪽
    queue.extend([row[i] for row in board[i+1:n-i-1]][::-1]) 	# 왼쪽

    queue.rotate(-r)  # r번만큼 반시계 회전

    # 1차원 배열을 다시 2차원 배열로 만들기
    for j in range(i, m-i):                 # 위쪽
        answer[i][j] = queue.popleft()
    for j in range(i+1, n-i-1):             # 오른쪽
        answer[j][m-i-1] = queue.popleft()
    for j in range(m-i-1, i-1, -1):           # 아래쪽
        answer[n-i-1][j] = queue.popleft()
    for j in range(n-i-2, i, -1):           # 왼쪽
        answer[j][i] = queue.popleft()

for i in range(n):
    for j in range(m):
        print(answer[i][j], end=' ')
    print()
