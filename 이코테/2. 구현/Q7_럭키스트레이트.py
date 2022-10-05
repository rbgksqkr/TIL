import sys
input = sys.stdin.readline


n = input().strip()
length = len(n)

left = sum(map(int, list(n[:length//2])))
right = sum(map(int, list(n[length//2:])))

if left == right:
    print("LUCKY")
else:
    print("READY")
