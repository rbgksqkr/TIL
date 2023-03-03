import sys
input = sys.stdin.readline

price = int(input())
result = 1000 - price
count = 0
types = [500, 100, 50, 10, 5, 1]

for type in types:
    count += result // type
    result %= type
print(count)
