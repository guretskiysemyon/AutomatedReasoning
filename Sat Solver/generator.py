
import random

def generate_random_sat_formula(num_variables, num_clauses, max_clause_length):
    formula = []
    variables = []
    for i in range(1, num_variables + 1):
        variables.append(random.choice([-1,1]) * i)

    formula.append(variables)

    for j in range(num_clauses):
        clause_length = random.randint(1, max_clause_length)
        # sign_bit = random.randint()
        clause = [random.choice([1, -1]) *  random.choice(variables) for _ in range(clause_length)]
        formula.append(clause)

    return formula



def write_to_cnf_file(filename, formula, variables, clauses):
    with open(filename, 'w') as file:
        file.write(f'p cnf {variables} {clauses + 1}\n')

        for clause in formula:
            file.write(' '.join(map(str, clause)) + ' 0\n')




# Example usage:
var_numbers = random.randint(1, 50)
num_clauses = random.randint(1, 100)
max_clause_length = random.randint(1, 20)

random_formula = generate_random_sat_formula(var_numbers, num_clauses, max_clause_length)



write_to_cnf_file("formula.cnf", random_formula, var_numbers, num_clauses)
       

