import sys
input = sys.stdin.readline
data = input().strip()
reversedData = data[::-1]
if data == reversedData:
    print(1)
else:
    print(0)
