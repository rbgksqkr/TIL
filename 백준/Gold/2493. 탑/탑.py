# --- 요구 사항 ---
# TODO: 탑들의 개수 N과 탑들의 높이가 주어질 때, 각각의 탑에서 발사한 레이저 신호를 어느 탑에서 수신하는가?
# 일직선 위에 N개의 높이가 서로 다른 탑을 수평 직선의 왼쪽부터 오른쪽 방향으로 차례로 세우고, 각 탑의 꼭대기에 레이저 송신기를 설치
# 모든 탑의 레이저 송신기는 레이저 신호를 지표면과 평행하게 수평 직선의 왼쪽 방향으로 발사
# 탑의 기둥 모두에는 레이저 신호를 수신하는 장치 설치
# 하나의 탑에서 발사된 레이저 신호는 가장 먼저 만나는 단 하나의 탑에서만 수신 가능
# --- 풀이 방법 ---
# N은 1 이상 500,000 이하. (N^2) 불가능 -> 3% 시간초과
# 정렬 X -> 이분탐색 X
# 어떻게 O(N) 또는 O(NlogN) 으로 순회하는가?
# --- 힌트 ---
# towers에서 비교할 탑을 1개씩 선택한다.
# 작은 탑들은 없애고 큰 탑들만 남겨놓기
# 현재 비교할 탑의 높이가 stack의 높이보다 낮으면 pop, 높으면 기록하고 push, break
# 뒤에 있는 탑을 push하기 때문에 앞에서 레이더에 걸리는 탑들이 새로 push한 탑에서도 걸림
# stack : [현재 타워의 인덱스, 높이]


import sys
input = sys.stdin.readline

n = int(input())
towers = list(map(int, input().split()))
answer = [0 for _ in range(n)]
stack = []
for i in range(n):
    while stack:
        if stack[-1][1] < towers[i]:  # 현재 타워의 높이가 가장 가까운 타워보다 더 높을 때
            stack.pop()
        else:  # 현재 타워의 높이가 가장 가까운 타워보다 더 낮을 때 (레이더에 걸릴 때)
            answer[i] = stack[-1][0] + 1 # 인덱스는 0부터 시작하므로 인덱스 + 1
            break
    stack.append([i, towers[i]])  # [현재 타워의 인덱스, 높이] : 자기 자신은 무조건 stack에 추가

print(*answer)
