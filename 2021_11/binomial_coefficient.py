from itertools import combinations  
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
numbers = [_ for _ in range(1, N+1)]
print(len(list(combinations(numbers, K))))
