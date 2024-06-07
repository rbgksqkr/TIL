import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    line = input().strip()
    print(line[0] + line[-1])
