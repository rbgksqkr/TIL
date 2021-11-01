N = int(input())
my_list = []
for i in range(N):
  my_list.append(input())
my_set = set(my_list)
alpha = list(my_set)
alpha.sort()
alpha.sort(key=lambda x : len(x))

for i in alpha:
  print(i)
