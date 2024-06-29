# --- 문제 분석 ---
# 빌딩에서 문서를 훔칠 예정. 평면도에는 문서의 위치가 모두 있음.
# 빌딩의 문은 모두 잠겨있기 때문에, 문을 열려면 '열쇠'가 필요하다.
# 상근이는 일부 열쇠를 이미 가지고 있고, 일부 열쇠는 빌딩의 바닥에 놓여져 있다.
# 상근이는 상하좌우로만 이동할 수 있다.
# --- 평면도 ---
# '.'는 빈 공간을 나타낸다.
# '*'는 벽을 나타내며, 상근이는 벽을 통과할 수 없다.
# '$'는 상근이가 훔쳐야하는 문서이다.
# 알파벳 대문자는 문을 나타낸다.
# 알파벳 소문자는 열쇠를 나타내며, 그 문자의 대문자인 모든 문을 열 수 있다.
# 마지막 줄에는 상근이가 이미 가지고 있는 열쇠가 공백없이 주어진다. 만약, 열쇠를 하나도 가지고 있지 않는 경우에는 "0"이 주어진다.
# a(열쇠)를 갖고 있으면, A(문)를 열 수 있음

# 상근이는 처음에는 빌딩의 밖에 있으며, 빌딩 가장자리의 벽이 아닌 곳을 통해 빌딩 안팎을 드나들 수 있다.
# 각각의 문에 대해서, 그 문을 열 수 있는 열쇠의 개수는 0개 이상이고, 각각의 열쇠에 대해서, 그 열쇠로 열 수 있는 문의 개수도 0개 이상이다.
# 열쇠는 여러 번 사용할 수 있다.

# TODO: 상근이가 훔칠 수 있는 문서의 최대 개수

# --- 문제 풀이 ---
# 1. 빌딩에 들어갈 인덱스 결정
# - 벽이 아닌 빌딩 가장자리 모든 케이스 체크 필요
# - 빌딩에 들어가는 지점을 하나의 케이스로 봤을 때 max값 비교 필요
# 2. 열쇠를 dict로 관리
# - if keys[board[mx][my]]: 이동
# - if board[mx][my] == '$': count ++
from collections import deque

dr = [-1, 0, 1, 0]  # 상 우 하 좌
dc = [0, 1, 0, -1]  # 상 우 하 좌


def bfs(visited):
    global ans

    queue = deque([[0, 0]])
    visited[0][0] = True
    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 범위를 벗어나거나 벽이거나 이미 방문했다면 컨티뉴
            if nc < 0 or nc >= w + 2 or nr < 0 or nr >= h + 2 or miro[nr][nc] == '*' or visited[nr][nc]:
                continue

            if 'A' <= miro[nr][nc] <= 'Z':  # 대문자라면(문이라면)
                if chr(ord(miro[nr][nc]) + 32) not in key:  # 해당 문을 열수있는 키가 없다면
                    continue  # 컨티뉴
            elif 'a' <= miro[nr][nc] <= 'z':  # 만약 소문자이고
                if miro[nr][nc] not in key:  # 아직 키에 없다면
                    key[miro[nr][nc]] = True  # 해당 키를 저장후
                    visited = [[False] * (w + 2)
                               for _ in range(h + 2)]  # 방문체크 초기화
            # 비밀문서이고 아직방문하지 않았다면
            elif miro[nr][nc] == "$" and (nr, nc) not in visited_doc:
                ans += 1  # 찾은 개수 1개 증가
                visited_doc.append((nr, nc))  # 해당 위치는 더이상 방문하면 안되기 때문에 저장

            visited[nr][nc] = True  # 방문처리
            queue.append([nr, nc])  # 다음 위치를 큐에 삽입


T = int(input())

for _ in range(1, T + 1):
    h, w = map(int, input().split())

    miro = ['.' + input() + '.' for _ in range(h)]
    miro = ['.' * (w + 2)] + miro + ['.' * (w + 2)]
    visited = [[False] * (w + 2) for _ in range(h + 2)]
    key = {}  # 가지고 있는 키 저장
    visited_doc = []  # 방문한 키 위치 저장

    for i in input():
        if i.isalpha():  # 만약 알파벳이면
            key[i] = True  # 키로 저장

    ans = 0
    bfs(visited)
    print(ans)
