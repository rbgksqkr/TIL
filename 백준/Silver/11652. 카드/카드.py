import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
dict = defaultdict(int)

for _ in range(n):
    num = int(input())
    dict[num] += 1

maxNum = max(dict.values())

result = sorted(dict.items(), key = lambda x: (-x[1], x[0]))
print(result[0][0])
 
