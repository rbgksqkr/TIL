import sys
input = sys.stdin.readline

s = list(map(int, list(input().strip())))
result = s[0]
for i in range(1, len(s)):
    result = max(result+s[i], result*s[i])
print(result)