from sys import stdin
from collections import deque



N, K = list(map(int, stdin.readline().split()))

people = deque(range(1, N+1))

print("<", end="")
while people:
  if len(people) == 1:
    print(str(people[0])+">")
    people.pop()
    break
  
  for i in range(1, K):
    people.rotate(-1)
  print(str(people[0])+", ", end="")
  people.popleft()


  
