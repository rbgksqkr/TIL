# 한 문자를 삭제하여 회문으로 만들 수 있는 문자열이라면 우리는 이런 문자열을 "유사회문"
# 1. 그 자체로 회문인지, 
# 2. 한 문자를 삭제하면 회문이 되는 “유사회문”인지, 
# 3. 회문이나 유사회문도 아닌 일반 문자열인지를 판단
# 문자열 그 자체로 회문이면 0, 유사회문이면 1, 그 외는 2를 출력

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  str_list = list(input().strip())
  n = len(str_list)
  flag = 0

  for i in range(n//2):
    start, end = i, n-i-1
    if str_list[start] != str_list[end]: # 양쪽이 다를 때
      # 왼쪽껄 버리고 팰린드롬 체크
      temp = str_list[:start] + str_list[start+1:]
      reversed_temp = temp[::-1]
      if temp == reversed_temp:
        flag = 1
        break
      # 오른쪽껄 버리고 팰린드롬 체크
      temp = str_list[:end] + str_list[end+1:]
      reversed_temp = temp[::-1]
      if temp == reversed_temp:
        flag = 1
        break
      # 양쪽 다 버려봐도 안되면 그냥 문자열
      else:
        flag = 2
        break
      
  # 원래 팰린드롬이였으면 첫 if문에 안걸려서 그대로 0 출력    
  print(flag)