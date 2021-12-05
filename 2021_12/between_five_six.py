import sys

input = sys.stdin.readline
A, B = map(str, input().split())

if "6" in A:
  A = A.replace("6", "5")
if "6" in B:
  B = B.replace("6", "5")
print(int(A)+int(B), end=" ")

if "5" in A:
  A = A.replace("5", "6")
if "5" in B:
  B = B.replace("5", "6")
print(int(A)+int(B))
