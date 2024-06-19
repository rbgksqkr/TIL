import sys
input = sys.stdin.readline
S = input().strip()
S = S.translate(str.maketrans('', '', 'CAMBRIDGE'))
print(S)