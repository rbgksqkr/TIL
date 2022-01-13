import sys
input = sys.stdin.readline

N = int(input())

# count = 0
# for _ in range(N):
#   visited = []
#   word = list(input().strip())
#   visited.append(word[0])
#   for i in range(1, len(word)):
#     if word[i] not in visited or word[i] == visited[-1]:
#       visited.append(word[i])
#     else:
#       break
  
#   if visited == word:
#     count += 1
  
# print(count)

count = 0
for _ in range(int(input())):
    text = input()
    if list(text) == sorted(text, key=text.find): # 단어 각각의 알파벳에 find 함수를 써서 인덱스순으로 정렬한다.
        count += 1

print(count)
