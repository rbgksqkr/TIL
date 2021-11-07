arr = input().split('-') # "-"를 기준으로 자른다
s = 0 
for i in arr[0].split('+'): # "-"가 나오기 전 문자열을 "+"기준으로 잘라 다 더한다
	s += int(i) 
for i in arr[1:]: 
    for j in i.split('+'): # "-"를 기준으로 잘랐기 때문에 arr 각각의 요소의 합을 모두 빼면 최솟값
    	s -= int(j) 
print(s)
