import sys
input = sys.stdin.readline

# 부분합이 S 이상이 되는 것 중, 가장 짧은 것
n, s = map(int, input().split())
arr = list(map(int, input().split()))
INF = int(1e9)

start, end = 0, 0
result = INF
total = arr[start]
while start <= end and end < n:
    if total < s:
        end += 1
        if end == n:
            break
        total += arr[end]
    else:
        result = min(result, end-start+1)
        total -= arr[start]
        start += 1
        
if result == INF:
    print(0)
else:
    print(result)