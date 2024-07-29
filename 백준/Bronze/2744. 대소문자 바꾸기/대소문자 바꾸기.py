strList = list(input().strip())

for idx, s in enumerate(strList):
    if s.isupper():
        strList[idx] = s.lower()
    else:
        strList[idx] = s.upper()


print(''.join(strList))
