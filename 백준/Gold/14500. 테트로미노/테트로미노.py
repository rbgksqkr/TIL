import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
visited = [[0 for _ in range(m)] for _ in range(n)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, L, result):
    global answer

    # 남은 재귀를 max_value로 돌아도 지금까지의 최댓값보다 작으면 종료
    if result + max_value * (4-L) <= answer:
        return

    if L == 4:
        answer = max(answer, result)
        return

    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]

        if mx < 0 or my < 0 or mx >= n or my >= m:
            continue

        if visited[mx][my] == 0:
            if L == 2:  # ㅗ, ㅜ, ㅓ, ㅏ 만들기
                visited[mx][my] = 1
                dfs(x, y, L+1, result+graph[mx][my])
                visited[mx][my] = 0
            visited[mx][my] = 1
            dfs(mx, my, L+1, result+graph[mx][my])
            visited[mx][my] = 0


max_value = 0
for i in range(n):
    max_value = max(max_value, max(graph[i]))

answer = 0
for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, 1, graph[i][j])
        visited[i][j] = 0
print(answer)