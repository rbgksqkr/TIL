# N×N인 지도. 길은 총 2N개.
# 길 : 한 행 또는 한 열 전부를 나타내며, 한쪽 끝에서 다른쪽 끝까지 지나가는 것
# 길을 지나갈 수 있으려면 높이가 같거나 경사로를 놓아서 지나갈 수 있는 길을 만들 수 있다.
# 경사로는 높이가 항상 1이며, 길이는 L이다.
# 경사로는 낮은 칸에 놓으며, L개의 연속된 칸에 경사로의 바닥이 모두 접해야 한다.
# 낮은 칸과 높은 칸의 높이 차이는 1이어야 한다.
# 경사로를 놓을 낮은 칸의 높이는 모두 같아야 하고, L개의 칸이 연속되어 있어야 한다.

# 지나갈 수 있는 길의 개수는? -> 모든 경우의 수 세기
# --- 풀이 방법 ---
# 한쪽 끝에서 반대 끝까지 탐색
# 높은쪽에서 낮은쪽으로 이동하는 것만 고려하기 위해 양쪽 끝 비교하여 큰 곳에서 출발
# 높이가 1차이 이하면 큐에 넣는다
# 경사로를 놓고 있는 상황인지 방문 배열에 별도로 저장
# 저장한 값이 L과 같아지면 계속 탐색, 같아지기 전에 탐색이 끝나거나(범위를 벗어남) 높이가 다른 곳을 만나면 return

# --- 문제 해석 오류로 다시 풀이 작성 ---
# 한쪽 끝에서 반대 끝까지 탐색하는데, 높이가 1차이면 올라갈수도 있음
# 경사로를 놓고 있을 때
# - 높이가 다르면 return
# - 높이가 같으면 경사로 계속 놓기
# - 다음 턴에 경사로를 다 놓으면 경사로 초기화
# 높아지는 경우 놓기 전 공간 확보 필요. if graph[mx][my] > graph[x][y]:
# 낮아지는 경우 경사로 이후 공간 확보 필요. if graph[mx][my] < graph[x][y]:


# --- 문제 힌트 ---
# 낮아지는 경우 : 현재 높이 > 다음 높이 -> 오른쪽 높이가 L만큼 같은지 체크
# 높아지는 경우 : 현재 높이 < 다음 높이 -> 왼쪽 높이가 L만큼 같은지 체크
# 경사로를 놓을 때
# - 현재 높이와 다음 높이가 다르면 return
# - 이미 경사로를 놓은 곳이면 return
# - 위에 해당하지 않으면 경사로 놓기

import sys
input = sys.stdin.readline

n, l = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]


def check(line, L):
    visited = [0 for _ in range(n)]  # 경사로 놓고 있는지 체크
    for i in range(n-1):
        # 다음 높이와 현재 높이 비교

        # 다음 높이와 현재 높이 같으면 pass
        if line[i] == line[i+1]:
            continue

        # 현재 높이와 다음 높이의 차이가 1보다 클 때 return
        elif abs(line[i] - line[i+1]) > 1:
            return False

        # 현재 높이 > 다음 높이
        elif line[i] > line[i+1]:
            # 오른쪽 지도 체크
            next_height = line[i+1]
            for j in range(i+1, i+L+1):
                if 0 <= j < n:
                    # 경사로를 놓을 때 높이가 다르면 return
                    if next_height != line[j]:
                        return False

                    # 경사로를 놓고 있으면 return
                    if visited[j]:
                        return False

                    visited[j] = True
                else:
                    return False

        # 현재 높이 < 다음 높이
        elif line[i] < line[i+1]:
            # 왼쪽 지도 체크
            next_height = line[i]
            for j in range(i, i-L, -1):
                if 0 <= j < n:
                    # 경사로를 놓을 때 높이가 다르면 return
                    if next_height != line[j]:
                        return False

                    # 경사로를 놓고 있으면 return
                    if visited[j]:
                        return False

                    visited[j] = True
                else:
                    return False
    return True

answer = 0
# 가로 길 체크
for line in graph:
    if check(line, l):
        answer += 1

# 세로 길을 체크하기 위해 변환해서 넣어줌
for i in range(n):
    temp = []
    for j in range(n):
        temp.append(graph[j][i])
    if check(temp, l):
        answer += 1

print(answer)
