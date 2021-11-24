import sys
input = sys.stdin.readline

S = input()
zeroCount = 0
oneCount = 0
flag = int(S[0])
if flag == 0:
  zeroCount += 1
else:
  oneCount += 1

for i in range(1, len(S)-1):
  if S[i] == "0":
    if flag == 0:
      continue
    zeroCount += 1
    flag = 0
  else:
    if flag == 1:
      continue
    oneCount += 1
    flag = 1

if zeroCount < oneCount:
  print(zeroCount)
else:
  print(oneCount)
