aah = input()
ah = input()

#재환이가 더 길게 ah를 하면 병원에 갈 필요없음
if len(aah) < len(ah):
    print("no")
#짧으면 병원에 가야함
else:
    print("go")