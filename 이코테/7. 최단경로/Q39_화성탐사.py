import heapq

t = int(input())
for _ in range(t):
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    INF = int(1e9)
    distance = [[INF for _ in range(n)] for _ in range(n)]
    distance[0][0] = graph[0][0]
    heap = []
    heapq.heappush(heap, (graph[0][0], 0, 0))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while heap:
        dist, x, y = heapq.heappop(heap)

        if distance[x][y] < dist:
            continue

        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx < 0 or my < 0 or mx >= n or my >= n:
                continue

            cost = dist + graph[mx][my]
            if cost < distance[mx][my]:
                distance[mx][my] = cost
                heapq.heappush(heap, (cost, mx, my))

    print(distance[n-1][n-1])
