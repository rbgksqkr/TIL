import sys

input = sys.stdin.readline

docs = input().rstrip()
word = input().rstrip()

cur = 0
count = 0

while cur < len(docs):
  if docs.find(word, cur) == -1:
    break
  else:
    cur = docs.find(word, cur)
    count += 1
    cur += len(word)

print(count)
