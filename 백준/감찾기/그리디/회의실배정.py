import sys
input = sys.stdin.readline

n = int(input())

timetable = []
for _ in range(n):
    a, b = map(int, input().split())
    timetable.append([a, b])
timetable.sort(key=lambda x: (x[1], x[0]))

count = 1
end = timetable[0][1]
for i in range(1, n):
    if end <= timetable[i][0]:
        end = timetable[i][1]
        count += 1
print(count)
