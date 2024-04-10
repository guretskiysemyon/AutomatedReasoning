# importing system module for reading files
import sys

# import utility functions
from utils import get_terms, get_function_symbols

# import classses for parsing smt2 files
from pysmt.smtlib.parser import SmtLibParser
from six.moves import cStringIO

# import pysmt functions for creating formulas and terms
from pysmt.shortcuts import Not, Equals, Function, Solver


from union_find import UnionFind


# solver for uninterpreted functions
# we represent a cube as a list of literals
# returns two elements `b,c`:
# if `cube` is satisfiable, `b` is `True` and `c` is `None`.
# otherwise, `b` is `False` and `c` is a sub-list of
# `cube` such that `c` is already unsatisfiable.
# `c` consists of the literals that were used
# in the derivation.
# In some cases, `c` will be simply the same as `cube`.
# But in various cases, the derivation did not
# rely on all literals of `cube`, and in such cases,
# only those literals that were relied on would be a
# part of `c`.


# Function to extract function symbols from a cube
def functions_in_cube(cube):
    # Initialize an empty dictionary to store function symbols and their corresponding lists of values
    func = {}

    # Get a list of function symbols present in the cube
    lst_symbols = get_function_symbols(cube)

    # Initialize an empty list for each function symbol in the dictionary
    for f in lst_symbols:
        func[f] = []

    return func


"""
    Process constraints in a cube to determine its satisfiability at the top level.

    Arguments:
    uf -- Union-find class for tracking connected components
    cube -- List of constraints

    Returns:
    bool -- False if the function determines that the formula is unsatisfiable, True otherwise.
    dict -- A dictionary containing information about the processed constraints:
            "core": list -- Constraints used till now that influence the decision.
            "neq": list -- Negative constraints for future processing.
            "func": dict -- Dictionary where keys are function symbols and values are lists of instances
                            of these functions in the formula.
    """


def top_level(uf, cube):
    # initialization
    core = []
    neq = []
    func = functions_in_cube(cube)

    # Iterate over each constraint in the cube
    for c in cube:

        # Check if the constraint is a negation
        if c.is_not():
            # Extract left and right arguments from the negation
            left, right = c.args()[0].args()

            # If left and right are connected then we have conflict.
            # Add constraint to core and return.
            if uf.connected(left, right):
                core.append(c)
                return False, {"core": core, "neq": neq, "func": func}

            # Add to the core constraint that is not negative, because it has the potential to influence the decision.
            neq.append(c)
            continue

        # Add to core constraint that not negative, because it has a potential to influence disicion.
        core.append(c)
        left, right = c.args()

        # If one of the side of equation is function add it to func dict.
        if left.is_function_application():
            func[left.function_name()].append(left)
        elif right.is_function_application():
            func[right.function_name()].append(right)

        # Union two sides.
        uf.union(left, right)

    return True, {"core": core, "neq": neq, "func": func}


"""
    Congruence Closure step. Check all pairs for the same function symbol f(x), f(y).
    If x and y are in the same class, then union f(x), f(y).

    Arguments:
    uf -- Union-find class for tracking connected components
    func -- Dictionary where keys are function symbols and values are lists of instances
            of these functions in the formula.

    Returns: none
"""


def CongruenceClosure(uf, func):
    for f in func.values():
        n = len(f)
        for i in range(n):
            fx = f[i]
            for j in range(i, n):
                fy = f[j]
                if fx == fy:
                    continue
                if check_function_arguments(uf, fx.args(), fy.args()):
                    uf.union(fx, fy)


"""
    Check for every negative constraint if its arguments are in the same equivalence class.
    If they are, return False; otherwise, return True. During the function, update core.

    Arguments:
    uf -- Union-find class for tracking connected components
    neq -- List of negative constraints
    core -- List of constraints used till now that influence the decision

    Returns:
        bool - True if there were no conflicts and False otherwise.
"""


def negative_literals(uf, neq, core):
    for c in neq:
        left, right = c.args()[0].args()
        if uf.connected(left, right):
            core.append(c)
            return False
    return True


"""
    Calculate minimum core. It removes temporary constraints and runs uf_solver again.
    If the result is unsat then move to the next constraint else return it and move to the next.

    Arguments:
    core -- List of constraints used till now that influence the decision

    Returns:
        minimum_core -- Minimum core
"""


def minimum_core(core):
    minimum_core = list(core)
    for x in core:
        minimum_core.remove(x)
        res, core = uf_solver(minimum_core)
        if res:
            minimum_core.append(x)

    return minimum_core


"""
    Process constraints in a cube to determine its satisfiability at the top level.

    Arguments:
    cube -- List of constraints

    Returns:
    bool -- False if the function determines that the formula is unsatisfiable, True otherwise.
    minimum_core -- Minimum core
    """


def uf_solver(cube):
    # create union-find
    uf = UnionFind()
    uf.create_by_list(get_terms(cube))

    # run top level
    res, data = top_level(uf, cube)
    if not res:
        return False, minimum_core(data["core"])

    # run cc
    CongruenceClosure(uf, data["func"])

    # check negative constraints
    res = negative_literals(uf, data["neq"], data["core"])
    if not res:
        return False, data["core"]

    return True, None


# Check for some function that all it's argument are conected.
def check_function_arguments(union_find, arguments_l, arguments_r):
    n = len(arguments_r)
    for i in range(n):
        if not union_find.connected(arguments_l[i], arguments_r[i]):
            return False
    return True


# main function
def main():
    # read path from input

    path = sys.argv[1]
    
    
    try:
        core_size = sys.argv[2]
    except Exception:
        # Code to handle the exception
        core_size = ""

        
    with open(path, "r") as f:
        smtlib = f.read()

    # parse the smtlib file and get a formula
    parser = SmtLibParser()
    script = parser.get_script(cStringIO(smtlib))
    formula = script.get_last_formula()

    # we are assuming `formula` is a flat cube.
    # `cube` represents `formula` as a list of literals
    cube = formula.args()

    # check if sat or unsat and print result
    sat, core = uf_solver(cube)
    if sat:
        print("sat")
    else:
        print("unsat")
        print("-----")
        if core_size == "min":
            core = minimum_core(core)
        print("\n".join([str(x) for x in core]))


if __name__ == "__main__":
    main()
