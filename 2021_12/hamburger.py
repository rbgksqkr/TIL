import sys
input = sys.stdin.readline

N, K = map(int, input().split())
hambug = input()
count = 0
check = [0] * N
for i in range(N):
  if hambug[i] == "P":
    for j in range(-K,K+1):
      if i+j < 0 or i+j >= N:
        continue       
      if hambug[i+j] == "H" and check[i+j] == 0:
        check[i+j] = 1
        count += 1
        break

print(count)
