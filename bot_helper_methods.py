# method list:
from bot import run_bot, bot
from collections import defaultdict

def get_amt_filled(grid, pos, xlen, ylen):
  cnt = 0
  for i in range(pos[0], ylen):
    for j in range(pos[1], xlen):
      if grid[i][j] == -1:
        cnt += 1
  return cnt

def fill(grid, pos, xlen, ylen, val):
  for i in range(pos[0], ylen):
    for j in range(pos[1], xlen):
      if grid[i][j] == -1:
        grid[i][j] = val
  return grid
        
def get_worst_move(grid,xlen,ylen):
  res = defaultdict(lambda: -2)
  for i in range(ylen-1, -1, -1):
    for j in range(xlen-1, -1, -1):
      if i == 0 and j == 0:
        pass
      else:
        if grid[i][j] == -1:
          res[(i,j)] = get_amt_filled(grid, (i,j), xlen, ylen)

  best_pos = -1
  best_val = -1
  for k,v in res.items():
    if best_val == -1 or v < best_val:
      best_pos = k
      best_val = v
  return best_pos
      

def printGrid(grid):
  h = False
  print("------")
  xlen = len(grid[0])
  ylen = len(grid)
  for i in range(ylen):
    for j in range(xlen):
      if i == 0 and j == 0:
        print("a", end = " ")
      else:
        print (grid[i][j]+1, end = " ")
    print()
  print("------")
  print()

def cant_move(grid):
  cnt = 0
  for i in grid:
   for j in i:
     if j == -1 and cnt == 0:
       cnt = 1
     elif j == -1:
       return False
  return True

def run_game():
  xlen = 1.1
  ylen = 1.1
  while type(xlen) != int or type(ylen) != int:
    xlen, ylen = map(int, input("What would you like your x and y values to be (spaced ints please): ").split())
    if type(xlen) != int or type(ylen) != int:
      print("invalid lengths, try again")
  
  player = 3
  while player > 1:
    player = (int(input("What player would you like to be(1 or 2): ")) - 1)
    if player > 1:
      print("bad player, please try again")

      
  print("-----------")
  print("EPIK GAMEEE")
  print("-----------")
  print()
  grid = [[-1 for i in range(xlen)] for j in range(ylen)]
  bot_state = (player+1)%2
  if player == 1:
    move = run_bot(grid, xlen, ylen, 0)
    grid = fill(grid, move, xlen, ylen, bot_state)
  print("for each of your moves, input an x and y value of the cell you wish to take, single spaced from each other")
  print()
  while True:
    printGrid(grid)
    if cant_move(grid):
      print("You lose!")
      break
    move = tuple(map(int, input("your move: ").split()))
    grid = fill(grid, move, xlen, ylen, player)
    printGrid(grid)
    if cant_move(grid):
      print("You Win!")
      break
    print("bots move:")
    move = run_bot(grid, xlen, ylen, bot_state)
    # print(move)
    if move == -1:
      print("UNOPTIMAL")
      move = get_worst_move(grid,xlen,ylen)
    grid = fill(grid, move, xlen, ylen, bot_state)
    
    
#### 
def run_game_bots():
  xlen = 1.1
  ylen = 1.1
  while type(xlen) != int or type(ylen) != int:
    xlen, ylen = map(int, input("What would you like your x and y values to be (spaced ints please): ").split())
    if type(xlen) != int or type(ylen) != int:
      print("invalid lengths, try again")
  
  player = 3
  while player > 1:
    player = (int(input("What bot would you like to be(1 or 2): ")) - 1)
    if player > 1:
      print("bad player, please try again")

      
  print("-----------")
  print("EPIK GAMEEE")
  print("-----------")
  print()
  grid = [[-1 for i in range(xlen)] for j in range(ylen)]
  bot_state = (player+1)%2
  if player == 1:
    move = run_bot(grid, xlen, ylen, 0)
    grid = fill(grid, move, xlen, ylen, bot_state)
  print("for each of your moves, input an x and y value of the cell you wish to take, single spaced from each other")
  print()
  while True:
    printGrid(grid)
    if cant_move(grid):
      print("You lose!")
      break
    move = run_bot(grid, xlen, ylen, player)
    if move == -1:
      print("UNOPTIMAL")
      move = get_worst_move(grid,xlen,ylen)
    print("bot 1's move:")
    grid = fill(grid, move, xlen, ylen, player)
    printGrid(grid)

    
    if cant_move(grid):
      print("You(the bot you chose) Win!")
      break
    print("bot 2's move:")
    move = run_bot(grid, xlen, ylen, bot_state)
    # print(move)
    if move == -1:
      print("UNOPTIMAL")
      move = get_worst_move(grid,xlen,ylen)
    grid = fill(grid, move, xlen, ylen, bot_state)
  
    