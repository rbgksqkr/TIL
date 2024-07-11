# 쿼터(Quarter, $0.25)의 개수, 다임(Dime, $0.10)의 개수,
# 니켈(Nickel, $0.05)의 개수, 페니(Penny, $0.01)의 개수
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    money = int(input())
    for i in [25, 10, 5, 1]:

        print(money//i, end=' ')
        money = money % i
    print()
