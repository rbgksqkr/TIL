import sys
input = sys.stdin.readline

n = int(input())
ext_dic = {}
for _ in range(n):
    a, ext = map(str, input().strip().split('.'))
    if ext in ext_dic:
        ext_dic[ext] += 1
    else:
        ext_dic[ext] = 1
    

ext_dic = sorted(ext_dic.items(), key=lambda x: x[0])
for ext, count in ext_dic:
    print(ext, count)