
import sys
import subprocess

for i in range(1000):
    # # Run experiment.py
    experiment_result = subprocess.run(["python3", "generator.py"], capture_output=True, text=True)

    # Run sat_solver.py (assuming it is an executable)
    sat_solver_result = subprocess.run(["python3","./sat_solver.py", "formula.cnf"], capture_output=True, text=True)

    # Run minisat on formula.cnf (assuming minisat is installed)
    minisat_result = subprocess.run(["minisat", "formula.cnf"], capture_output=True, text=True)

    # Compare results
    if sat_solver_result.returncode != minisat_result.returncode:
    #     print("All results are the same.")
    #     sys.exit(0)  # Indicate success
    # else:
        print("Results differ.")
        sys.exit(1)  # Indicate an error