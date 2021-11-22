import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  N = int(input())
  count = 0
  applicant = []
  for _ in range(N):
    a, b = map(int, input().split())
    applicant.append((a, b))
  
  applicant.sort()
  
  minRank = applicant[0][1]
  for i in range(len(applicant)):
    if minRank > applicant[i][1]:
      minRank = applicant[i][1]
    if minRank < applicant[i][1]:
      count += 1
  print(N - count)
