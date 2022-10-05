import sys
input = sys.stdin.readline
n = int(input())
students = []
for _ in range(n):
    name, ko, en, mat = input().split()
    ko, en, mat = int(ko), int(en), int(mat)
    students.append((name, ko, en, mat))

students.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))

for i in range(n):
    print(students[i][0])