# --- 요구사항 ---
# N×N 크기의 땅. r과 c는 1부터 시작. r이 행, c가 열.
# 땅의 양분을 조사하는 로봇. 1×1 크기의 칸에 들어있는 양분을 조사해 상도에게 전송하고, 모든 칸에 대해서 조사를 한다.
# 가장 처음에 양분은 모든 칸에 5만큼 들어있다.
# 나무 재테크 : 작은 묘목을 구매해 어느정도 키운 후 팔아서 수익을 얻는 재테크
# M개의 나무를 구매해 땅에 심었다. 한 칸에 여러 개의 나무가 심어져 있을 수도 있다.

# - 봄
# 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가한다.
# 각각의 나무는 나무가 있는 1×1 크기의 칸에 있는 양분만 먹을 수 있다.
# 하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다.
# 만약, 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽는다.

# - 여름
# 봄에 죽은 나무가 양분으로 변하게 된다.
# 각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가된다. 소수점 아래는 버린다.

# - 가을
# 나무가 번식한다.
# 번식하는 나무는 나이가 5의 배수이어야 하며, 인접한 8개의 칸에 나이가 1인 나무가 생긴다.
# 어떤 칸 (r, c)와 인접한 칸은 (r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1) 이다.
# 상도의 땅을 벗어나는 칸에는 나무가 생기지 않는다.

# - 겨울
# 로봇이 땅을 돌아다니면서 땅에 양분을 추가한다.
# 각 칸에 추가되는 양분의 양은 A[r][c]이고, 입력으로 주어진다.

# TODO: K년이 지난 후 상도의 땅에 살아있는 나무의 개수?

# --- 풀이 방법 ---
# 1. 봄, 여름, 가을, 겨울에 양분 상태 변경 함수를 만든다.
# 봄 - 나무들의 나이 저장. 어린 나이부터 양분을 먹고, 안죽으면 나이 += 1, 죽으면 죽은 나무 배열에 추가해 반환
# 여름 - 죽은 나무 배열을 받아 나이를 2로 나눈 값을 양분으로 추가(Math.floor)
# 가을 - 나이가 5의 배수인 나무 찾기. 인접 칸에 나이가 1인 나무 심기.
# 겨울 - 땅에 입력값으로 주어진 양분 추가.


import sys
from collections import deque

input = sys.stdin.readline
N, M, K = map(int, input().split())

# 양분 5 기본값
energyBoard = [[5]*N for _ in range(N)]

# 추가 양분 배열
addEnergyBoard = [list(map(int, input().split())) for _ in range(N)]
treeBoard = [[deque() for _ in range(N)] for _ in range(N)]
# treeList = []
for _ in range(M):
    x, y, age = list(map(int, input().split()))
    # treeList.append([x-1, y-1, age])
    treeBoard[x-1][y-1].append(age)
# treeList.sort(key=lambda x: x[2])  # 어린 나무부터 양분 먹는다


def spring_summer():
    global energyBoard
    for i in range(N):
        for j in range(N):
            tree_count = len(treeBoard[i][j])
            for k in range(tree_count):
                if energyBoard[i][j] >= treeBoard[i][j][k]:
                    energyBoard[i][j] -= treeBoard[i][j][k]
                    treeBoard[i][j][k] += 1
                else:
                    for _ in range(k, tree_count):
                        energyBoard[i][j] += treeBoard[i][j].pop() // 2
                    break


def fall_winter():
    for i in range(N):
        for j in range(N):
            for age in treeBoard[i][j]:
                if age % 5 == 0:
                    for k in range(8):
                        mx = i + dx[k]
                        my = j + dy[k]

                        if mx < 0 or my < 0 or mx >= N or my >= N:
                            continue

                        treeBoard[mx][my].appendleft(1)

            energyBoard[i][j] += addEnergyBoard[i][j]


# def spring(treeList):
#     next_treeList = []
#     die_treeList = []
#     for tree in treeList:
#         x, y, age = tree
#         if energyBoard[x][y] - age >= 0:
#             energyBoard[x][y] -= age
#             next_treeList.append([x, y, age+1])
#         else:
#             die_treeList.append([x, y, age])
#     return next_treeList, die_treeList


# def summer(die_treeLIst):
#     for tree in die_treeLIst:
#         x, y, age = tree
#         energyBoard[x][y] += age // 2


# def fall(treeList):
#     additional_treeList = []
#     for tree in treeList:
#         x, y, age = tree
#         if age % 5 == 0:
#             for i in range(8):
#                 mx = x + dx[i]
#                 my = y + dy[i]

#                 if mx < 0 or my < 0 or mx >= N or my >= N:
#                     continue

#                 additional_treeList.append([mx, my, 1])
#     return additional_treeList + treeList


# def winter():
#     for i in range(N):
#         for j in range(N):
#             energyBoard[i][j] += addEnergyBoard[i][j]


dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]


for _ in range(K):
    spring_summer()
    fall_winter()

# for _ in range(K):
#     treeList, die_treeLIst = spring(treeList)
#     summer(die_treeLIst)
#     treeList = fall(treeList)
#     winter()

answer = 0
for i in range(N):
    for j in range(N):
        answer += len(treeBoard[i][j])
print(answer)
