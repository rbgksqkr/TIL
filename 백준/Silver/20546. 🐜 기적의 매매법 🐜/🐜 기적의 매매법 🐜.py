import sys
input = sys.stdin.readline

n = int(input())
prices = list(map(int, input().split()))
final_price = prices[-1]

jun_money = n
jun_count = 0
for price in prices:
    jun_count += jun_money // price
    jun_money %= price

sung_money = n
sung_count = 0
inc, desc, prev = 0, 0, 0
for price in prices:
  if price > prev:
    inc += 1
    desc = 0
    if inc >= 3:
      if sung_count > 0:
        sung_money += sung_count * price
        sung_count = 0
      inc = 0
  elif price < prev:
    desc += 1
    inc = 0
    if desc >= 3:
        sung_count += sung_money // price
        sung_money %= price
        inc = 0
  prev = price
    

jun_total = jun_money + jun_count * final_price
sung_total = sung_money + sung_count * final_price

if jun_total > sung_total:
    print('BNP')
elif jun_total < sung_total:
    print('TIMING')
else:
    print('SAMESAME')