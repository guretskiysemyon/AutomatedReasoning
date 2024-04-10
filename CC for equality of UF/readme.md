
## Explanation
We have implemented the Congruence Closure algorithm to determine if a formula from the Equality fragment of First Order Logic is satisfiable. It returns 'sat' if the formula is satisfiable and 'unsat' otherwise. Additionally, it provides the core of the formula that renders it unsatisfiable. We have also included a naive implementation for finding the minimum core of the formula, as described below.

### How to Run?

#### Packages
You must install the `pysmt` library and the `z3` solver for this exercise. You can read more about them in their documentation:
[PySMT GitHub](https://github.com/pysmt/pysmt)

#### Run the File

To run your implementation, use the following command:

```
python3 uf_solver.py <path-to-smt2>
```

where `<path-to-smt2>` is the path to an smt2 file.

For example:

```
python3 uf_solver.py benchmarks/uf1.smt2
```

The expected result should look like this:

```
unsat
----
<lit1>
<lit2>
...
```

We have also implemented a naive core search for this formula. If you wish to find the minimum core, you should add "min" to the passing arguments:

```
python3 uf_solver.py <path-to-smt2> min
```
