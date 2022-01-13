import sys
input = sys.stdin.readline

N = int(input())
count = 0
for _ in range(N):
  visited = []
  word = list(input().strip())
  visited.append(word[0])
  for i in range(1, len(word)):
    if word[i] not in visited or word[i] == visited[-1]:
      visited.append(word[i])
    else:
      break
  
  if visited == word:
    count += 1
  
print(count)
