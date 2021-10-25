word = input().upper()
mydic = {}
for i in word:
  if i in mydic.keys():
   mydic[i] += 1
  else:
    mydic[i] = 1

maxs = [k for k,v in mydic.items() if max(mydic.values()) == v]

if len(maxs) > 1:
  print("?")
else:
  print(maxs[0])
