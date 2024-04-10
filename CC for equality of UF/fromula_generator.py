import random


def declare_variables(num_variables):
    declarations = ""
    for i in range(1, num_variables + 1):
        declarations += f"(declare-fun x{i} () S)\n"
    return declarations


def declare_functions(num_functions):
    declarations = ""
    for i in range(1, num_functions + 1):
        declarations += f"(declare-fun f{i} (S) S)\n"
    return declarations


def generate_assertions(num_variables, max_num_assertions, num_functions):
    assertions = ""
    num_assertions = random.randint((max_num_assertions * 3) // 4, max_num_assertions)
    for _ in range(num_assertions):
        var1 = random.randint(1, num_variables)
        var2 = random.randint(1, num_variables)
        while var2 == var1:
            var2 = random.randint(1, num_variables)
        assertions += f"(assert (= x{var1} x{var2}))\n"

    num_assertions = random.randint((max_num_assertions) // 4, max_num_assertions // 2)
    for _ in range(num_assertions // 2):
        var1 = random.randint(1, num_variables)
        var2 = random.randint(1, num_variables)
        while var2 == var1:
            var2 = random.randint(1, num_variables)
        assertions += f"(assert (not (= x{var1} x{var2})))\n"

    num_assertions = random.randint((max_num_assertions) // 4, max_num_assertions)
    for _ in range(num_assertions):
        var1 = random.randint(1, num_variables)
        assertions += f"(assert (= (f{random.randint(1, num_functions)} x{var1}) x{random.randint(1, num_variables)}))\n"

    return assertions


def generate_random_formula(num_variables, num_assertions, num_functions):
    script = "(set-logic QF_UF)\n"
    script += "(declare-sort S 0)\n"
    script += declare_variables(num_variables)
    script += declare_functions(num_functions)
    script += generate_assertions(num_variables, num_assertions, num_functions)
    script += "(check-sat)"
    return script


# Example usage:
num_variables = 20
num_assertions = 10
num_functions = 5
random_script = generate_random_formula(num_variables, num_assertions, num_functions)
f = open("uf.smt2", "w")
f.write(random_script)
