import sys
input = sys.stdin.readline

data = input().strip()
data = list(map(int, list(data)))
data.sort(reverse=True)
answer = ''.join(list(map(str, data)))
print(answer)
