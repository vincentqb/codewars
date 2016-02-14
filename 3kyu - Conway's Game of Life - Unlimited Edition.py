def convert_table_to_dict(table):
    ni = len(table)
    nj = len(table[0])
    
    dict = {}
    for i in range(ni):
      for j in range(nj):
        if table[i][j] == 1:
          dict[(i,j)] = None
          
    return dict

def convert_dict_to_table(dict):

  keys = dict.keys()
  
  if not keys:
    mi = mj = ni = nj = 0
  else:
    mi = min(map(lambda x: x[0], keys))
    mj = min(map(lambda x: x[1], keys))
    ni = max(map(lambda x: x[0], keys))
    nj = max(map(lambda x: x[1], keys))
  
  table = [[0 for j in range(nj-mj+1)] for i in range(ni-mi+1)]
  
  for (i,j) in keys:
    table[i-mi][j-mj] = 1
  
  return table
  
from itertools import product
def get_generation(cells, generations):

  cells_dict = convert_table_to_dict(cells)

  for n in range(generations):
    
    stack = {}
    cells_new = {}
    
    for (i,j) in cells_dict:
      for (di, dj) in product((-1,0,1), (-1,0,1)):
        stack[(i+di,j+dj)] = None
    
    for (i,j) in stack:
      neighbours = 0
      for (di, dj) in product((-1,0,1), (-1,0,1)):
        if (i+di,j+dj) in cells_dict and (di,dj) != (0,0):
          neighbours += 1
        
      if neighbours == 3:
        cells_new[(i,j)] = None
      elif neighbours == 2 and (i,j) in cells_dict:
        cells_new[(i,j)] = None
          
    cells_dict = cells_new
          
  return convert_dict_to_table(cells_dict)
