temp = float(input())
while True :
    next = float(input())
    if next == 999 : break
    print("{:.2f}".format(next - temp))
    temp = next
