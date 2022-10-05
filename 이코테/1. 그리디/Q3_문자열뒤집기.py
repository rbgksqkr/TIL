import sys
input = sys.stdin.readline

s = input().strip()

flag = 0
zero_count, one_count = 0, 0
if s[0] == '0':
    flag = 0
    zero_count += 1
else:
    flag = 1
    one_count += 1

for i in range(1, len(s)):
    if s[i] == '1' and flag == 0:
        flag = 1
        one_count += 1
    elif s[i] == '0' and flag == 1:
        flag = 0
        zero_count += 1

print(min(zero_count, one_count))