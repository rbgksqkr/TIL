n = int(input())
stores = list(map(int, input().split()))

d = [0 for _ in range(101)]

# k-1번째를 털면 k번째는 못텀
# k-2번째를 털면 k번째 털 수 있음
# k-3번째부터는 k-1번째와 같은 케이스이므로 고려하지 않아도 됨.

for i in range(n):
    d[i+1] = stores[i]

for i in range(3, n+1):
    d[i] = max(d[i-1], d[i]+d[i-2])

print(d[n])

# 4
# 1 3 1 5