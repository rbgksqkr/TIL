import sys
input = sys.stdin.readline
n = int(input())

members = {}

for _ in range(n):
    name, type = map(str, input().split())

    if type == 'enter':
        members[name] = 1
    if type == 'leave':
        del members[name]


result = list(members.keys())
result.sort(reverse=True)
for key in result:
    print(key)
