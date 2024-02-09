
# importing system module for reading files
import sys

# in what follows, a *formula* is a collection of clauses,
# a clause is a collection of literals,
# and a literal is a non-zero integer.




# input path:  a path to a cnf file
# output: the formula represented by the file, 
#         the number of variables, 
#         and the number of clauses
def parse_dimacs_path(path):
  clauses = []
  num_variables = 0
  num_clauses = 0

  with open(path, 'r') as file:
      for line in file:
          tokens = line.strip().split()

          if not tokens:
              continue

          if tokens[0] == 'c':
              # Ignore comments
              continue
          elif tokens[0] == 'p':
              # Found problem line, extract number of variables and clauses
              num_variables = int(tokens[2])
              num_clauses = int(tokens[3])
          else:
              # Add clause to the list
              clause = [int(token) for token in tokens[:-1]]
              clauses.append(clause)

  return clauses, num_variables, num_clauses, 
  # return [], 0, 0

def check_clauses_naive(cnf, binary_string):
  for c in cnf:
      satisfied = False
      for x in c:
        if x > 0 and binary_string[x] == "1":
            satisfied = True
            break
        elif x < 0 and  binary_string[-x] == "0":
            satisfied = True
            break
            
      if not satisfied:
        return False
  return True
    
            



   

# input cnf: a formula
# input n_vars: the number of variables in the formula
# input n_clauses: the number of clauses in the formula
# output: True if cnf is satisfiable, False otherwise
def naive_solve(cnf, n_vars, n_clauses):
  for i in range(2 ** (n_vars + 1)):
        binary_string = bin(i)[2:].rjust(n_vars + 1, '0')
        print(binary_string)
        if check_clauses_naive(cnf, binary_string):
           return True, binary_string
  return False, ""



def unit_propagate(cnf, M, possible_D):
  is_changed = True
  while is_changed:
    is_changed = False
    for clause in cnf:
      flag = False
      unass = []

      for x in clause:
        if x in M:
          flag = True
          break
        elif -x not in M:
          unass.append(x)
      

      if not flag and len(unass) == 1:
        is_changed = True
        M.append(unass[0])
        possible_D.remove(abs(unass[0]))
    
  return M
    



def check_clauses_dpll(cnf, M):
    for clause in cnf:
      flag = False
      for x in clause:
          if x in M or -x not in M:
            flag = True
            break
      if not flag:
        return False
      flag = False
    return True
    

def backtrack(M, D, possible_D):
    last_decide = D.pop()
    i = len(M) - 1
    while M[i] != last_decide:
       possible_D.add(abs(M.pop()))
       i -= 1
    
    M.pop()
    M.append(-last_decide)
    return M
    

# input cnf: a formula
# input n_vars: the number of variables in the formula
# input n_clauses: the number of clauses in the formula
# output: True if cnf is satisfiable, False otherwise
def dpll_solve(cnf, n_vars, n_clauses):
  M = []
  D = []
  possible_D = set(list(range(1, n_vars + 1)))
 
  while True:
      M = unit_propagate(cnf, M, possible_D)
      b = check_clauses_dpll(cnf, M)
      if b and len(M) == n_vars:
          M.insert(0, 0)
          return True, M
      elif not b and len(D) == 0:
          return False, None
      elif not b:
         M = backtrack(M, D, possible_D)
      else:
          new_ass = possible_D.pop()
          D.append(new_ass)
          M.append(new_ass)
         

          
      

  
 
def print_assigment_dpll(res, assignment):
    if not res:
      print("unsat")
      return
    print("sat")
    n = len(assignment)
    for i in range(1,n):
      if assignment[i] >  0:
        print(f"{i}: true")
      else:
        print(f"{i}: false")


def print_assigment_naive(res, assignment):
    if not res:
      print("unsat")
      return
    print("sat")
    n = len(assignment)
    for i in range(1,n):
      if assignment[i] == "1":
        print(f"{i}: true")
      else:
        print(f"{i}: false")

######################################################################


# get path to cnf file from the command line
path = sys.argv[1]

# get algorithm from the command line
algorithm = sys.argv[2]


# make sure that algorithm is either "naive" or "dpll"
assert(algorithm in ["naive", "dpll"])

# parse the file
cnf, num_vars, num_clauses = parse_dimacs_path(path)

res = False

# check satisfiability based on the chosen algorithm
# and print the result
if algorithm == "naive":
  res, assignment = naive_solve(cnf, num_vars, num_clauses)
  print_assigment_naive(res, assignment)
else:
  res, assignment = dpll_solve(cnf, num_vars, num_clauses)
  print_assigment_dpll(res, assignment)


          