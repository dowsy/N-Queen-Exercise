# The N Queen is the problem of placing N chess queens on an N×N chessboard so that no two queens attack each other. For example, following is a solution for 4 Queen problem.
# The expected output is a binary matrix which has 1s for the blocks where queens are placed. For example, following is the output matrix for above 4 queen solution.

#               { 0,  1,  0,  0}
#               { 0,  0,  0,  1}
#               { 1,  0,  0,  0}
#               { 0,  0,  1,  0}


#My solutions below
global N 
N = 5
#fill in '0's for the whole board
board = [[0 for i in range(N)]for i in range(N)]

def check_diag(a,b,dir_x,dir_y):
  vec = []
  x = a
  y = b
  while (x+dir_x in range(N) and y + dir_y in range(N)):
    vec.append([x+dir_x, y+dir_y])
    x += dir_x
    y += dir_y
  return vec
  
def check_hor(x,y):
  for i in range(N):
    if board[i][y] == 1:
      return False
  return True

def load_diag(a,b):
  for i in (
  check_diag(a,b,-1,-1) #check left-up 
  + check_diag(a,b,-1,1) #check left-down
  + check_diag(a,b,1,-1) #check right-up
  + check_diag(a,b,1,1) #check right-down
  ):
    if board[i[0]][i[1]] == 1:
      return False
  return True

def check_safe(x,y):
  if ((1 not in board[x]) and check_hor(x,y) and load_diag(x,y) and board[x][y]==0):
    return True
  return False

def place_queen(board, queens_no):
  if queens_no >= N:
    return True
  for i in range(N):
    for j in range(N):
      if check_safe(i,j):
        board[i][j] = 1
        #check if the next queen can be placed and recur
        if place_queen(board, queens_no+1) == True:
          return True
        board[i][j] = 0
  # if cannot be placed in any 'j' return False
  return False

if place_queen(board,0) == False:
  print("No solution")
else:
  print(board)
