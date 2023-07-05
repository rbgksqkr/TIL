import sys
input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(input().strip()))

def getResult(graph):
    max_value = 1
    for i in range(N):
        result = 1
        for j in range(1, N):
            if graph[i][j] == graph[i][j-1]:
                result += 1
            else: 
                result = 1
            max_value = max(max_value, result)

        result = 1
        for j in range(1, N):
            if graph[j][i] == graph[j-1][i]:
                result += 1
            else:
                result = 1
            max_value = max(max_value, result)
    return max_value

# def getResult(data):
#     max_cnt = 1
#     for i in range(N):
#         cnt = 1
#         for j in range(1, N):
#             if data[i][j] == data[i][j-1]:
#                 cnt += 1
#             else:
#                 cnt = 1
#             max_cnt = max(max_cnt, cnt)

#         cnt = 1
#         for j in range(1, N):
#             if data[j][i] == data[j-1][i]:
#                 cnt += 1
#             else:
#                 cnt = 1
#             max_cnt = max(max_cnt, cnt)
    
#     return max_cnt

answer = 0
for i in range(N):
    for j in range(N):
        if j+1 < N:
            graph[i][j], graph[i][j+1] = graph[i][j+1], graph[i][j]
            answer = max(answer, getResult(graph))
            graph[i][j], graph[i][j+1] = graph[i][j+1], graph[i][j]
        if i+1 < N:
            graph[i][j], graph[i+1][j] = graph[i+1][j], graph[i][j]
            answer = max(answer, getResult(graph))
            graph[i][j], graph[i+1][j] = graph[i+1][j], graph[i][j]

print(answer)