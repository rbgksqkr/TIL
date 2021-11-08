import sys

input = sys.stdin.readline
N = int(input())
ropes = []
for i in range(N):
  ropes.append(int(input()))

ropes.sort(reverse=True)
result = []
for i in range(N): 
  result.append(ropes[i]*(i+1))

print(max(result))
