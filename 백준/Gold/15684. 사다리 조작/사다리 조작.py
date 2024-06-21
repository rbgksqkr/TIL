# --- 요구 사항 ---
# N개의 세로선과 M개의 가로선
# 가로선은 인접한 두 세로선을 연결해야 한다.
# - 단, 두 가로선이 연속하거나 서로 접하면 안 된다. 또, 가로선은 점선 위에 있어야 한다.
# 사다리에 가로선을 추가해서, 사다리 게임의 결과를 조작하려고 한다.
# - 이때, i번 세로선의 결과가 i번이 나와야 한다.
# TODO: 추가해야 하는 가로선 개수의 최솟값? 3보다 큰 값이면 -1 출력. 또, 불가능한 경우에도 -1 출력.

# --- 문제 풀이 ---
# 1. 각각의 번호가 현재 사다리 상태에서 어디에 도착할지 찾기
# 2. 선을 추가했을 때 변경될 도착지점 구하기
# 3. 추가할 가로선의 최소 개수를 구한다 (2 ≤ N ≤ 10, 1 ≤ H ≤ 30, 0 ≤ M ≤ (N-1)×H)
# - 어디에 추가해야 최소가 될 지를 어떻게 알지?
# - 몇 개가 최소일지 어떻게 알지?

# [0][1] -> 세로선 1의 1번째 인덱스 저장
# [1][1] -> 세로선 1의 2번째 인덱스 저장

import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())
board = [[0]*N for _ in range(H)]

for _ in range(M):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1  # 왼쪽에서 오른쪽으로 가는 경우만 저장


def isCorrect():  # i번 세로선의 결과가 i번이 나오는지 여부 확인
    for i in range(N):
        now = i
        for j in range(H):
            if board[j][now]:
                now += 1
            elif now > 0 and board[j][now-1]: # 오른쪽에서 왼쪽으로 가는 가로선이 존재
                now -= 1

        if i != now:
            return False
    return True


def dfs(count, x, y):
    global answer
    if isCorrect():
        answer = min(answer, count)
        return

    if count == 3 or answer <= count:
        return

    for i in range(x, H):
        if i == x:  # 행 변경 x
            now = y
        else:  # 행 변경 o -> 처음부터 탐색
            now = 0
        for j in range(now, N-1):
            if not board[i][j]: # 가로선이 없다면
                board[i][j] = 1 # 가로선을 긋고
                dfs(count + 1, i, j+2) # 안겹치도록 2칸 점프
                board[i][j] = 0 # 백트래킹


answer = 4
dfs(0, 0, 0)
if answer < 4:
    print(answer)
else:
    print(-1)
