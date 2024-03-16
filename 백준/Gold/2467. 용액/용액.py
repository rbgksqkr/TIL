import sys
input = sys.stdin.readline

n = int(input())
attributes = list(map(int, input().split()))
start, end = 0, n - 1

answer = abs(attributes[start] + attributes[end])
answer_start = start
answer_end = end

while start < end:
    total = attributes[start] + attributes[end]
    if answer > abs(total):
        answer_start = start
        answer_end = end
        answer = abs(total)
        if answer == 0:
            break

    if total < 0:
        start += 1
    else:
        end -= 1


print(attributes[answer_start], attributes[answer_end])
