# --- 문제 분석 ---
# 2차원 평면상에 N(3 ≤ N ≤ 10,000)개의 점으로 이루어진 다각형
# TODO: 다각형의 면적?

# --- 문제 풀이 ---
# 다각형 면적 구하기 공식
# 1/2|x1y2-x2y1 + x2y3-x3y2 ... + xny1-x1yn|


import sys
input = sys.stdin.readline

n = int(input())
vertex = []
sumNum = 0
for _ in range(n):
    x, y = map(int, input().split())
    vertex.append([x, y])
vertex.append(vertex[0])

for i in range(n):
    x, y = vertex[i]
    mx, my = vertex[i+1]

    sumNum += x*my-y*mx


answer = (1/2)*abs(sumNum)
print(round(answer, 2))
