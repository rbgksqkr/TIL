import sys
input = sys.stdin.readline

m = int(input())

data = set()

for _ in range(m):
    command = input().split()
    if len(command) == 1:
        if command[0] == 'all':
            data = set([i for i in range(1, 21)])
        if command[0] == 'empty':
            data = set()
    else:
        x = int(command[1])

        if command[0] == 'add':
            data.add(x)
        if command[0] == 'remove':
            data.discard(x)
        elif command[0] == 'check':
            print(1 if x in data else 0)
        elif command[0] == 'toggle':
            if x in data:
                data.discard(x)
            else:
                data.add(x)
