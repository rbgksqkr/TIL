import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    r, e, c = map(int, input().split())

    total = r + c

    if e == total:
        print('does not matter')
    elif e > total:
        print('advertise')
    else:
        print('do not advertise')
