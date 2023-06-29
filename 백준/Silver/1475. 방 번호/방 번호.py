import sys
import math
input = sys.stdin.readline

N = input().strip()
mystr = list(N)
mydic = {}
for i in mystr:
    if mydic.get(i):
        mydic[i] += 1
    else:
        mydic[i] = 1

if mydic.get('6') and mydic.get('9'):
    mydic['6'] += mydic['9']
    del mydic['9']
sorted_dic = sorted(mydic.items(), key=lambda x: -x[1])
if sorted_dic[0][0] == '6' or sorted_dic[0][0] == '9':
    first = math.ceil(sorted_dic[0][1]/2)
    if len(sorted_dic) > 1 and first < sorted_dic[1][1]:
        print(sorted_dic[1][1])
    else:
        print(first)
else:
    print(sorted_dic[0][1])