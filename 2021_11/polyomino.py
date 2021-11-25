import sys
board = sys.stdin.readline()
count = 0

for i in range(len(board)):
  if board[i] == "X":
    count += 1

  elif board[i] == "." or i == len(board)-1:
    if count >= 6:
      count_four = count // 4
      count = count % 4
      count_two = count // 2
      count = count % 2
      if count == 0:
        if count_four:
          board = board.replace("X", "A", count_four*4)
        if count_two:
          board = board.replace("X", "B", count_two*2)  
        count = 0

    if count > 0 and count % 4 == 0:
      board = board.replace("X", "A", 4)
      count = 0
    elif count > 0 and count % 2 == 0:
      board = board.replace("X", "B", 2)
      count = 0

if count:
  print(-1)
else:
  print(board.strip())
