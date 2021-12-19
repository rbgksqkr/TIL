import sys
input = sys.stdin.readline

answer = 0
G = int(input())
P = int(input())
parent = [i for i in range(G + 1)]
planes = []

for _ in range(P):
    planes.append(int(input()))

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


for plane in planes:
    docking = find(plane)
    if docking == 0:
        break
    parent[docking] = parent[docking - 1]
    answer += 1
print(answer)
