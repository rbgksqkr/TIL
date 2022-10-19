n, m = map(int, input().split())
balls = list(map(int, input().split()))
weights = [0] * (m+1)
for ball in balls:
    weights[ball] += 1

total = sum(weights)
answer = 0
for i in range(1, m+1):
    if weights[i]:
        total -= weights[i]
        answer += total * weights[i]
print(answer)
    
