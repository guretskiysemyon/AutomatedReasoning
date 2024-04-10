## Explanation
This exercise solves formulas in CNF (Conjunctive Normal Form) using a naive approach and the DPLL (Davis-Putnam-Logemann-Loveland) algorithm, without employing any heuristics.

## How to Run
### Packages
In general no packages needed, but if you wish to run tests, you will need to install the Minisat solver, or you can modify the test code to use any other solver you prefer.

### Run the File
Use the following command to run the solver:

```python3 sat_solver.py <path-to-cnf> <algorithm>```
where `<algorithm>` can be either "naive" or "dpll".

### Tests
There are two files for tests:

1. Generator: This script attempts to generate random formulas in CNF form and writes them to a file named "formula.cnf".

2. Tests: This script runs the generator to create "formula.cnf", then it executes our simple solver and the Minisat solver, comparing their results. To automate this process fully, we recommend removing print statements and modifying the sat_solver.py file to return values instead.
To run the automatic tests, you need to change the sat_solver.py file. We've kept it as is because it meets the exercise's requirements. However, you can easily modify the files for a more customized approach.
