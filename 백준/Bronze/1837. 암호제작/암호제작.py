import sys
input = sys.stdin.readline

p, k = map(int, input().split())

answer = True
for i in range(2, k):
    if p % i == 0:
        answer = False
        print('BAD', i)
        break
if answer:
    print('GOOD')
