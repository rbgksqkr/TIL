import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = set(a)
b = set(b)
diff = list(a-b)

diff.sort()
print(len(diff))

for i in diff:
    print(i, end=' ')
