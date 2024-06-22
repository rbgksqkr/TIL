import sys
input = sys.stdin.readline

parens = list(input().strip())

answer = 10
for i in range(1, len(parens)):
    if parens[i] == parens[i-1]:
        answer += 5
    else:
        answer += 10
print(answer)
