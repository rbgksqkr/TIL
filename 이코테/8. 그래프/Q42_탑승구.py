import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


g = int(input())
p = int(input())
parent = [i for i in range(g+1)]
result = 0
entrances = []
for _ in range(p):
    entrances.append(int(input()))

for entrance in entrances:
    data = find(parent, entrance)
    if data == 0:
        break
    union(parent, data, data-1)
    result += 1

print(result)

# 4
# 6
# 2
# 2
# 3
# 3
# 4
# 4

########## O(n^2)로 시간초과 ############
# import sys
# input = sys.stdin.readline

# G = int(input()) # 탑숭구 수
# P = int(input()) # 비행기 수

# visited = [0 for _ in range(G+1)]
# entrances = []
# for _ in range(P):
#     entrances.append(int(input()))

# count = 0
# for entrance in entrances:
#     flag = 0
#     for i in range(entrance, 0, -1):
#         if visited[i] == 0:
#             visited[i] = 1
#             count += 1
#             flag = 1
#             break
    
#     if flag == 0:
#         break

# print(count)




