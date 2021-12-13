import sys
input = sys.stdin.readline
N = int(input())
weight_limits = list(map(int, input().split()))
M = int(input())
boxes = list(map(int, input().split()))
visited = [0 for _ in range(len(boxes))]
count = 0

weight_limits.sort(reverse=True)
boxes.sort(reverse=True)

if weight_limits[0] < boxes[0]:
  print(-1)
else:
  while boxes:
    for i in range(N):
      for j in range(len(boxes)):
        if weight_limits[i] >= boxes[j]:
          boxes.remove(boxes[j])
          break
    count += 1

  print(count)
