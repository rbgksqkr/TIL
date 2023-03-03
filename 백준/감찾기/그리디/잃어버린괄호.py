import sys
input = sys.stdin.readline

arr = input().strip().split('-')

for i in range(len(arr)):
    a = list(map(int, arr[i].split('+')))
    arr[i] = sum(a)
result = arr[0]
for i in range(1, len(arr)):
    result -= arr[i]
print(result)
