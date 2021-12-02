import heapq
import sys

input = sys.stdin.readline
N = int(input())

timeTable = [list(map(int, input().split())) for _ in range(N)]
timeTable.sort(key=lambda x: x[0])

queue = []
heapq.heappush(queue,timeTable[0][1])

for i in range(1,N):
    if queue[0] > timeTable[i][0]: # 진행중인 강의 중 가장 빠른 강의가 끝나기 전에 다음 강의가 있을 때
        heapq.heappush(queue,timeTable[i][1])
    else: # 이전 강의 뒤에 그 강의실에서 다음 강의를 진행할 수 있을 때
        heapq.heappop(queue)
        heapq.heappush(queue,timeTable[i][1])

print(len(queue))
