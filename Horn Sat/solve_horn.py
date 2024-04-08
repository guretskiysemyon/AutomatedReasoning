







# def parse_dimacs_path(path):
#     clauses = []
#     num_variables = 0
#     num_clauses = 0

#     with open(path, "r") as file:
#         for line in file:
#             tokens = line.strip().split()

#             if not tokens:
#                 continue

#             if tokens[0] == "c":
#                 # Ignore comments
#                 continue
#             elif tokens[0] == "p":
#                 # Found problem line, extract number of variables and clauses
#                 num_variables = int(tokens[2])
#                 num_clauses = int(tokens[3])
#             else:
#                 # Add clause to the list
#                 clause = [int(token) for token in tokens[:-1]]
#                 clauses.append(clause)

#     return (
#         clauses,
#         num_variables,
#         num_clauses,
#     )





# def is_horn_sat_quad(clauses, num_variables):
#     queue = []
#     var_val = [False] * (num_variables + 1)


#     up_clauses = []
#     # Initialization
#     for c in clauses:
#         if len(c) == 1:
#             l = c[0]
#             var_val[abs(l)] = l > 0
#             queue.append(l)
#         else:
#             up_clauses.append(c)




#     while queue:
#         clauses = up_clauses
#         up_clauses = []
#         curr = queue.pop()
#         for cl in clauses:
#             if (-curr) in cl:
#                 cl.remove(-curr)
#                 if len(cl) == 1:
#                     l = cl[0]
#                     var_val[abs(l)] = l > 0
#                     queue.append(l)
#                 elif len(cl) == 0:
#                     return "unsat", None
#                 else:
#                     up_clauses.append(cl)
#             elif curr not in cl:
#                 up_clauses.append(cl)

#     return "sat", var_val
        
    
            
            







# if __name__ == "__main__":
#     path = "C:\\Users\\semka\\Code Projects\\Code Projects\\Horn Sat\\benchmarks\\03.cnf"
#     clauses, num_var, num_claus = parse_dimacs_path(path)
#     print(clauses)
#     res, ass = is_horn_sat_quad(clauses, num_var)
#     print(res)
#     if res == "sat":
#         print(ass)


def parse_dimacs_path(path):
    clauses = []  # List to hold clauses, which are sets
    num_variables = 0
    num_clauses = 0

    with open(path, "r") as file:
        for line in file:
            tokens = line.strip().split()

            if not tokens:
                continue

            if tokens[0] == "c":
                # Ignore comments
                continue
            elif tokens[0] == "p":
                # Found problem line, extract number of variables and clauses
                num_variables = int(tokens[2])
                num_clauses = int(tokens[3])
            else:
                # Add clause to the list, as a set
                clause = {int(token) for token in tokens[:-1]}
                clauses.append(clause)

    return clauses, num_variables, num_clauses

def is_horn_sat_quad(clauses, num_variables):
    queue = set()
    var_val = [False] * (num_variables + 1)

    up_clauses = []  # Use a list to store clauses since we need to iterate over them
    # Initialization
    for c in clauses:
        if len(c) == 1:
            l = next(iter(c))  # Get the single element from the set
            var_val[abs(l)] = l > 0
            queue.add(l)
        else:
            up_clauses.append(c)

    while queue:
        clauses = up_clauses
        up_clauses = []
        curr = queue.pop()
        for cl in clauses:
            if (-curr) in cl:
                cl.remove(-curr)
                if len(cl) == 1:
                    l = next(iter(cl))
                    var_val[abs(l)] = l > 0
                    queue.add(l)
                elif len(cl) == 0:
                    return "unsat", None
                else:
                    up_clauses.append(cl)
            elif curr not in cl:
                up_clauses.append(cl)

    return "sat", var_val







if __name__ == "__main__":
    path = "C:\\Users\\semka\\Code Projects\\Code Projects\\Horn Sat\\benchmarks\\01.cnf"
    clauses, num_var, num_claus = parse_dimacs_path(path)
    print(clauses)
    res, ass = is_horn_sat_quad(clauses, num_var)
    print(res)
    if res == "sat":
        print(ass)


