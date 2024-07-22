import sys
input = sys.stdin.readline

n = int(input())

answer = 0
k = 1
while True:

    if n == 0:
        break
    if n < k:
        k = 1
        continue
    else:
        n -= k

    answer += 1
    k += 1

print(answer)
