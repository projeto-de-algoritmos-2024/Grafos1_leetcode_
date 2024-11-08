import pulp as plp
import numpy as np

prob = plp.LpProblem("SolverNQueens", sense=plp.const.LpMinimize)

# Set the objective function
# Sudoku works only on the constraints
# There is no objective function that we are trying maximize or minimize.
# Set a dummy objective


rows = range(0,8)
cols = range(0,8)
values = range(0,1)


# Decision Variable/Target variable
grid_vars = plp.LpVariable.dicts("grid_value", (rows,cols), cat='Binary')
#Calculando valor pro objetivo:
objective = plp.lpSum([grid_vars[row][col]*(row+col) for row, col in zip(rows, cols)])
prob.setObjective(objective)





# Regras

# CONSTRAINT 2: Constraint to ensure that values from 1 to 9 is filled only once in a row

#Contraint: Apenas uma rainha pode estar na mesma linha

for row in rows:
        prob.addConstraint(plp.LpConstraint(e=plp.lpSum([grid_vars[row][col] for col in cols]),
                                    sense=plp.LpConstraintEQ, rhs=1, name=f"constraint_uniq_row_{row}_{values}"))

# CONSTRAINT 3: Apenas uma rainha pode estar na mesma coluna:
for col in cols:
        prob.addConstraint(plp.LpConstraint(e=plp.lpSum([grid_vars[row][col] for row in rows]),
                                    sense=plp.LpConstraintEQ, rhs=1, name=f"constraint_uniq_col_{col}_{values}"))

diagonais = []
diagonal = []
for sum_diagonal in range(15):
  for row in rows:
     for col in cols:
       if (row + col) == sum_diagonal:
        #print(f'({row},{col}) ', end='')
        diagonal.append((row,col))
  diagonais.append(diagonal)
  diagonal = []
  #print(diagonais)

for sum_diagonal in range(-7, 8):
  for row in rows:
     for col in cols:
       if (row - col) == sum_diagonal:
        #print(f'({row},{col}) ', end='')
        diagonal.append((row,col))
  diagonais.append(diagonal)
  diagonal = []
  #print(diagonais)

# Para todas as lista que possuerem o encontro de rainhas
for diagonal in diagonais:
  prob.addConstraint(plp.LpConstraint(e=plp.lpSum([grid_vars[row][col] for row,col in diagonal]),
                                    sense=plp.LpConstraintLE, rhs=1, name=f"constraint_uniq_diagonal_{diagonal}_{values}"))






print(f'Solution Status = {plp.LpStatus[prob.status]}')

# Code to extract the final solution grid
solution = [[0 for col in cols] for row in rows]
grid_list = []
for row in rows:
    for col in cols:
      if plp.value(grid_vars[row][col]):
        solution[row][col] = 1

# Print the final solution as a grid
print(f"\nFinal result:")

for row in rows:
    print("\n",end="\n  ")
    for col in cols:
        num_end = "   "
        print(solution[row][col],end=num_end)






diagonais = []
diagonal = []
for sum_diagonal in range(15):
  for row in rows:
     for col in cols:
       if (row + col) == sum_diagonal:
        #print(f'({row},{col}) ', end='')
        diagonal.append((row,col))
  diagonais.append(diagonal)
  diagonal = []
  #print(diagonais)





for sum_diagonal in range(-7, 8):
  for row in rows:
     for col in cols:
       if (row - col) == sum_diagonal:
        #print(f'({row},{col}) ', end='')
        diagonal.append((row,col))
  diagonais.append(diagonal)
  diagonal = []
  print(diagonais)
  




matrix = np.arange(9).reshape((3,3))

print(matrix.diagonal(0))
print(matrix.diagonal(-1))
print(matrix.diagonal(-2))
print(matrix.diagonal(3))