import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lines = []
for _ in range(m):
    package, each = map(int, input().split())
    lines.append([package, each])
package_line = sorted(lines, key=lambda x: x[0])
each_line = sorted(lines, key=lambda x: x[1])

min_cost = int(1e9)
if package_line[0][0] <= each_line[0][1]*6:
    count = n // 6
    left = n % 6
    min_cost = min(package_line[0][0] * count + each_line[0]
                   [1] * left, package_line[0][0] * (count+1))
else:
    min_cost = each_line[0][1] * n
print(min_cost)
