import sys
input = sys.stdin.readline

rankDic = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0,
    'P': 0.0,
}

total = 0
total_completed_count = 0
for _ in range(20):
    title, GPA, rank = input().split()
    GPA = float(GPA)
    total += GPA * rankDic[rank]
    if rank != 'P':
        total_completed_count += GPA

print(round(total / total_completed_count, 6))
