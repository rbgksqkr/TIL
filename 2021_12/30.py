N = list(input())
N.sort(reverse=True)

int_numbers = list(map(int, N))

if sum(int_numbers) % 3 != 0 or int_numbers[-1] != 0:
  print(-1)
else:
  print(''.join(N))
