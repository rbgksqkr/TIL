import sys
input = sys.stdin.readline

n = int(input())
data = []
pos = -1

for _ in range(n):
    op = input().split()
    if op[0] == 'push':
        data.append(op[1])
        pos += 1
    elif op[0] == 'pop':
        if pos == -1:
            print(-1)
        else:
            print(data.pop())
            pos -= 1
    elif op[0] == 'size':
        print(len(data))
    elif op[0] == 'empty':
        if len(data) == 0:
            print(1)
        else:
            print(0)
    elif op[0] == 'top':
        if len(data) == 0:
            print(-1)
        else:
            print(data[-1])
