from pysmt.shortcuts import Solver, And, Or, Not, BOOL, Symbol, TRUE, Implies
import sys
import os




def strong_strip(string):
    res = ""
    for x in string:
        if not x.isspace():
            res += x

    return res


def parse_package_file(file_path):
    package_data = {}
    install_list = set()

    with open(file_path, 'r') as file:
        current_package = None

        for line in file:
            line = strong_strip(line)

            if line.startswith('Package:'):
                current_package = line.split(':')[1]
                package_data[current_package] = {}
            elif line.startswith('Depends:'):
                package_data[current_package]['Depends'] = line.split(':')[1]
            elif line.startswith('Conflicts:'):
                package_data[current_package]['Conflicts'] = line.split(':')[1]
            elif line.startswith('Install:'):
                install_list.update(line.split(':')[1:][0].split(','))


    return package_data, install_list



def get_variable(v_name):
    t = variables_dic.get(v_name)
    if t:
        return t
    
    new = Symbol(v_name, BOOL)
    variables_dic[v_name] = new
    return new



def create_expression(dep_line):
    dep_line = dep_line.split(',')
    formulaes = []
    for x in dep_line:
        if  '|' in x:
            vars = x.split('|') # May be can be more
            queue_install.update(vars)
            ors = []
            for y in vars:
                ors.append(get_variable(y))
            formulaes.append(Or(ors))
        else:
            queue_install.add(x)
            formulaes.append(get_variable(x))

    return formulaes



def install_package(package_name):

    package_data = package_dictionary.pop(package_name)
    depends = package_data.get("Depends")
    if depends:
        formulaes = create_expression(package_data["Depends"])
        expr = Implies(get_variable(package_name), And(formulaes) )
        assertions.append(expr)
        solver.add_assertion(expr)
    
    conflict = package_data.get("Conflicts")
    
    if not conflict:
        return


    formulaes = create_expression(conflict)
    ex = Or(formulaes) # OR
    expr = Implies(get_variable(package_name) , Not(Or(formulaes)))
    assertions.append(expr)
    solver.add_assertion(expr)

    completed_packages.add(package_name)




def print_instalation_program():
    for var, symbol in variables_dic.items():
        if solver.get_value(symbol) == TRUE():
            print(var)
    
    
    




    
def preprocessing():
    for x in queue_install:
        var_x = Symbol(x, BOOL)
        variables_dic[x] = var_x
        solver.add_assertion(var_x)
        assertions.append(x)


    while len(queue_install) != 0:
        current_package = queue_install.pop()
        if current_package in completed_packages:
            continue

        if current_package in package_dictionary:
            install_package(current_package)
        else:
            get_variable(current_package)    

# for x in assertions:
#     print(x)




if len(sys.argv) != 2:
    print("Wrong number of arguments.")
    sys.exit(1)

filename = sys.argv[1]
if not os.path.exists(filename):
    print(f"File not found: {filename}")
    sys.exit(1)
    


solver = Solver(name="z3")

# path = 'ex1.dep'

# Dictionary from parsering the file and list of needed instalations.
package_dictionary, queue_install  = parse_package_file(filename)

# We want to save the variables that we've already created symbol for them.
variables_dic = {}

completed_packages = set()

assertions = []

preprocessing()

# for x in queue_install:
#     var_x = Symbol(x, BOOL)
#     variables_dic[x] = var_x
#     solver.add_assertion(var_x)
#     assertions.append(x)


# while len(queue_install) != 0:
#     current_package = queue_install.pop()
#     if current_package in completed_packages:
#         continue

#     if current_package in package_dictionary:
#         install_package(current_package)
#     else:
#         get_variable(current_package)
    


# for x in assertions:
#     print(x)


res = solver.check_sat()
# print("Res ", res)
if not res:
    print("There is no installation plan")
else:
    print("There is an installation plan:")
    print_instalation_program()

