def bot(grid, xlen, ylen, layer):
  state = (layer+1)%2
  for y in range(ylen):
    for x in range(xlen):
      if y == x and y == 0:
        pass
      elif grid[y][x] == -1:
        g2 = g2 = [g[:] for g in grid]
        g2[y][x] = state
        for i in range(y, ylen):
          for j in range(x, xlen):
            if g2[i][j] == -1:
              g2[i][j] = state
        val = bot(g2, xlen, ylen, layer+1)
        if val == state:
          # print((x,y))
          return val
  return not state

def run_bot(ga, xlen, ylen, state):
  grid = [g[:] for g in ga]
  for y in range(ylen):
    for x in range(xlen):
      if y == x and y == 0:
        pass
      elif grid[y][x] == -1:
        g2 = [g[:] for g in grid]
        g2[y][x] = state
        for i in range(y, ylen):
          for j in range(x, xlen):
            if g2[i][j] == -1:
              g2[i][j] = state
              
        val = bot(g2, xlen, ylen, state + 1)
        if val != state:
          return (y,x)
  return -1
  



# def get_all_Moves(ga, xlen, ylen, state):
#   grid = 


# the game runs on 1's and 2's, but for the sake of binary simplicity, the normal 1 is represented as 0 and the normal 2 is represented by 1
# to use
# runbot takes 4 params:
# grid: the current grid so far. -1 in all blank spaces(including top-left), 1's in positions of player 2's moves, 0's in positions of player 1's moves. when rendering, maybe display everything on the grid + 1? idk. all values are ints. 
# xlen: the width of the grid
# ylen: the height of the grid
# state: the player that the bot is playing as(0 for player 1, 1 for player 2)


