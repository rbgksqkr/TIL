import sys
input = sys.stdin.readline

S = input().strip()
input_data = list(S)
data = [0 for _ in range(26)]

for i in input_data:
    idx = ord(i)-ord('a')
    data[idx] += 1
for i in data:
    print(i, end=' ')