n = int(input())

students = {}
for _ in range(n):
    name, grade = input().split()
    grade = int(grade)
    students[name] = grade

student = sorted(students.items(), key=lambda x:x[1])
print(student)
for i in student:
    print(i[0], end=' ')


# 2
# 홍길동 95
# 이순신 77