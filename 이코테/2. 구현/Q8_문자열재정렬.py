import sys
from collections import deque
input = sys.stdin.readline

s = list(input().strip())
s.sort()
s = deque(s)
number = 0
while True:
    if s[0].isdigit():
        number += int(s.popleft())
    else:
        break

alpha = ''.join(list(s))

print(alpha+str(number))



# K1KA5CB7