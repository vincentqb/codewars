def spiralize(size):

  if size == 0:
    return []
  elif size == 1:
    return [[1]]
  elif size == 2:
    return [[1,1],[0,1]]
    
  spiral = [ [0 for i in range(size)] for j in range(size) ]
  
  # Make a snake
  iter = 0
  i = j = 0
  changed = True
  while changed:
    changed = False
    spiral[i][j] = 1
    if iter % 4 == 0:
      jold = j
      while j == size-2 or (j < size-2 and spiral[i][j+2] == 0): 
        j += 1
        spiral[i][j] = 1
        changed = True
      if abs(j - jold) == 1: break
    elif iter % 4 == 1:
      iold = i
      while i == size-2 or (i < size-2 and spiral[i+2][j] == 0):
        i += 1
        spiral[i][j] = 1
        changed = True
      if abs(i - iold) == 1: break
    elif iter % 4 == 2:
      jold = j
      while j == 1 or (j >= 2 and spiral[i][j-2] == 0):
        j -= 1
        spiral[i][j] = 1
        changed = True
      if abs(j - jold) == 1: break
    elif iter % 4 == 3:
      iold = i
      while i == 1 or (i >= 2 and spiral[i-2][j] == 0):
        i -= 1
        spiral[i][j] = 1
        changed = True
      if abs(i - iold) == 1: break
    iter += 1
  return spiral


print(spiralize(1) == [[1]])
print(spiralize(2) == [[1,1], [0,1]])
print(spiralize(3) == [[1,1,1],
                       [0,0,1],
                       [1,1,1]])
print(spiralize(5) == [[1,1,1,1,1],
                       [0,0,0,0,1],
                       [1,1,1,0,1],
                       [1,0,0,0,1],
                       [1,1,1,1,1]])
print(spiralize(8) == [[1,1,1,1,1,1,1,1],
                       [0,0,0,0,0,0,0,1],
                       [1,1,1,1,1,1,0,1],
                       [1,0,0,0,0,1,0,1],
                       [1,0,1,0,0,1,0,1],
                       [1,0,1,1,1,1,0,1],
                       [1,0,0,0,0,0,0,1],
                       [1,1,1,1,1,1,1,1]])
