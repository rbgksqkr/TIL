import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    golds = []
    dp = [[0 for _ in range(m)] for _ in range(n)]
    max_gold = 0

    temp = list(map(int, input().split()))
    for i in range(0, n*m, m):
        line = temp[i:i+m]
        golds.append(line)

    for i in range(n): # 시작위치 금의 크기를 dp테이블에 초기화
        dp[i][0] = golds[i][0]

    
    move = [(1, 1), (0, 1), (-1, 1)] # 오른쪽 위, 오른쪽, 오른쪽 아래
    for i in range(m):
        for j in range(n):
            x, y = j, i
            for k in range(3):
                dx = x + move[k][0]
                dy = y + move[k][1]

                if dx < 0 or dy < 0 or dx >= n or dy >= m:
                    continue
                
                dp[dx][dy] = max(dp[dx][dy], dp[x][y] + golds[dx][dy]) # (dx, dy)로 갈때 이전의 캐는 방식이랑 이번의 캐는 방식 비교
    
    for i in range(n):
        max_gold = max(max_gold, dp[i][-1]) # 도착하는 행들 중 금을 가장 많이 캔 방식을 채택
    print(max_gold)








# 2
# 3 4
# 1 3 3 2 2 1 4 1 0 6 4 7
# 4 4
# 1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
