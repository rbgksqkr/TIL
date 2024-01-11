import sys
input = sys.stdin.readline


def POW(a, b, m):
    if b == 1:
        return a % m
    val = POW(a, b//2, m)
    if b % 2 == 0:
        return (val * val) % m
    return (val * val * a) % m


a, b, c = map(int, input().split())
print(POW(a, b, c))
