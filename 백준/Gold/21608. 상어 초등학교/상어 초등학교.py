# --- 요구 사항 ---
# 교실은 N×N (3 ≤ N ≤ 20)
# 학생의 수 : N^2 명

# 각 학생이 좋아하는 학생 4명씩 조사
# 한 칸에는 학생 한 명의 자리만 있을 수 있고, 상하좌우에 있을 경우만 인접하다고 한다.

# 배치 방법
# - 1. 비어있는 칸 중 좋아하는 학생이 가장 많이 인접한 칸으로 자리를 정한다.
# - 2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
# - 3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.

# 학생의 만족도는 자리 배치가 모두 끝난 후에 구할 수 있다.
# 학생의 만족도를 구하려면 그 학생과 인접한 칸에 앉은 좋아하는 학생의 수를 구해야 한다.
# 그 학생과 인접한 칸에 앉은 좋아하는 학생의 수 : 0, 1, 2, 3, 4 -> 만족도 : 0, 1, 10, 100, 1000

# TODO: 학생의 만족도의 총 합
# --- 문제 풀이 ---
# 1. 자리 배치하기
# - 좋아하는 학생들의 인접한 칸에 체크를 하고, max값에 배치
# - max값이 여러개면, 그 칸과 인접한 칸 중 비어있는 칸이 가장 많은 칸으로 배치
# - 그런 칸도 여러 개면, 행의 번호가 작은 칸, 행이 같으면 열의 번호가 작은 칸으로 배치
# 2. 학생의 만족도 구하기
# - 인접한 칸에 앉은 좋아하는 학생의 수로 만족도 계산
# 3. 학생의 만족도 총합 구하기

import sys
input = sys.stdin.readline

n = int(input())

# n*n 책상 배치 저장
data = [[0] * n for _ in range(n)]

# [[해당 순서 사람, 좋아하는 사람 4명] ... ]
students = [list(map(int, input().split())) for _ in range(n**2)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for student in students:
    available = []

    for i in range(n):
        for j in range(n):
            # 빈자리가 있다면
            if data[i][j] == 0:
                prefer, empty = 0, 0  # prefer: 인접하는 좋아하는 사람 수,  empty: 인접하는 빈 칸 수

                # 동서남북 방향 확인하여
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    # 범위내에 있을 때
                    if 0 <= nx < n and 0 <= ny < n:
                        # 좋아하는 학생이 주위에 있다면 더해준다.
                        if data[nx][ny] in student[1:]:  # student[1:] : 좋아하는 사람 4명
                            prefer += 1

                        # 빈자리가 있다면 더해준다.
                        if data[nx][ny] == 0:
                            empty += 1

                available.append((i, j, prefer, empty))
    # 정렬
    # 1. 인접하는 좋아하는 사람 수, 2. 인접하는 빈 칸 수, 작은 행, 작은 열
    available.sort(key=lambda x: (-x[2], -x[3], x[0], x[1]))
    data[available[0][0]][available[0][1]] = student[0]

answer = 0
score = [0, 1, 10, 100, 1000]
students.sort()

for i in range(n):
    for j in range(n):
        count = 0

        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if 0 <= nx < n and 0 <= ny < n:
                if data[nx][ny] in students[data[i][j] - 1]:  # 인접한 위치에 좋아하는 사람이 있다면 만족도 += 1
                    count += 1

        answer += score[count]

print(answer)
