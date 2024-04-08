def parse_dimacs(file_path):
    with open(file_path, 'r') as file:
        clauses = []
        literal_to_clauses = {}  # Maps literals to their clauses
        for line in file:
            if line.startswith('c') or line.startswith('p'):
                continue
            parts = [int(x) for x in line.strip().split()[:-1]]
            negatives = set()
            positive = None
            clause_index = len(clauses)
            for part in parts:
                if part < 0:
                    literal = str(abs(part))
                    negatives.add(literal)
                    if literal not in literal_to_clauses:
                        literal_to_clauses[literal] = []
                    literal_to_clauses[literal].append(clause_index)
                else:
                    positive = str(part)
            clauses.append((negatives, positive))
        return clauses, literal_to_clauses

def linear_solve_horn_formula(clauses, literal_to_clauses):
    worklist = set()
    unsatisfied_counts = [len(clause[0]) for clause in clauses]
    true_literals = set()

    for i, (negatives, positive) in enumerate(clauses):
        if len(negatives) == 0 and positive is not None:
            true_literals.add(positive)
            worklist.add(positive)

    while worklist:
        current_literal = worklist.pop()
        if current_literal not in literal_to_clauses:
            continue
        for clause_index in literal_to_clauses[current_literal]:
            negatives, positive = clauses[clause_index]
            unsatisfied_counts[clause_index] -= 1
            if unsatisfied_counts[clause_index] == 0 and positive is not None:
                if positive not in true_literals:
                    true_literals.add(positive)
                    worklist.add(positive)

    for count in unsatisfied_counts:
        if count == 0 and clauses[unsatisfied_counts.index(count)][1] is None:  # Check for contradiction
            return 'UNSAT'
    return 'SAT'


# Example usage
file_path = "C:\\Users\\semka\\Code Projects\\Code Projects\\Horn Sat\\benchmarks\\01.cnf"
clauses, literal_t0_clasuses = parse_dimacs(file_path)
result = linear_solve_horn_formula(clauses, literal_t0_clasuses)
print(result)
