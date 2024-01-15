import sys
input = sys.stdin.readline

n, m = map(int, input().split())
INF = int(1e9)
count = INF
graph = []
cctv = []
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(m):
        if 1 <= line[j] <= 5:
            cctv.append([[i, j], line[j]])
    graph.append(line)


move = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]]
]

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def getArea(graph):
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                count += 1
    return count


def observer(cur, direction, graph):
    x, y = cur
    for d in direction:
        mx, my = x, y
        while True:
            mx += dx[d]
            my += dy[d]

            if mx < 0 or my < 0 or mx >= n or my >= m or graph[mx][my] == 6:
                break

            if graph[mx][my] == 0:
                graph[mx][my] = '#'


def dfs(depth, graph):
    global count
    graph_copy = [[j for j in graph[i]] for i in range(n)]

    if depth == len(cctv):
        count = min(count, getArea(graph))
        return

    cur, cctvNum = cctv[depth]

    for i in move[cctvNum]:
        observer(cur, i, graph_copy)
        dfs(depth+1, graph_copy)
        graph_copy = [[j for j in graph[i]] for i in range(n)]


dfs(0, graph)
print(count)
