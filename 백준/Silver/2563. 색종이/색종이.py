import sys
input = sys.stdin.readline

n = int(input())
papers = [[0 for _ in range(100)] for _ in range(100)]
count = 0
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            if papers[i][j] == 0:
                papers[i][j] = 1
                count += 1

print(count)