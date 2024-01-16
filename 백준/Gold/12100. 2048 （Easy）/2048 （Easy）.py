import sys
input = sys.stdin.readline

n = int(input())

graph = []
rotate_graph = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, input().split())))


# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# INF = int(1e9)
# answer = INF


# def getArea(graph):
#     global answer
#     for i in range(n):
#         answer = max(answer, max(graph[i]))


# def move(dir, graph):
#     dx[dir]

#     for i in range(n):
#         for j in range(n):
#             graph[i][j]

# def dfs(depth, dir, graph):
#     if depth == 5:
#         getArea(graph)
#         return

#     graph_copy = [[j for j in graph[i]] for i in range(n)]
#     for dir in range(4):
#         move(dir, graph_copy)
#         dfs(depth+1, dir, graph_copy)
#         graph_copy = [[j for j in graph[i]] for i in range(n)]


def rotate(graph):
    rotated_graph = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated_graph[i][j] = graph[n-j-1][i]
    return rotated_graph


def tilt(dir):
    global graph, rotate_graph
    while dir:
        rotate_graph = rotate(rotate_graph)
        dir -= 1

    for i in range(n):
        tilted = [0 for _ in range(n)]
        idx = 0
        for j in range(n):
            if rotate_graph[i][j] == 0:
                continue
            if tilted[idx] == 0:
                tilted[idx] = rotate_graph[i][j]
            elif tilted[idx] == rotate_graph[i][j]:
                tilted[idx] *= 2
                idx += 1
            else:
                idx += 1
                tilted[idx] = rotate_graph[i][j]
        for j in range(n):
            rotate_graph[i][j] = tilted[j]


mx = 0
for temp in range(1024):
    for i in range(n):
        for j in range(n):
            rotate_graph[i][j] = graph[i][j]
    brute = temp
    for i in range(5):
        dir = brute % 4
        brute = brute // 4
        tilt(dir)

    for i in range(n):
        for j in range(n):
            mx = max(mx, rotate_graph[i][j])
print(mx)
