## Explanation about exercise.

A dep file is partitioned into blocks. The blocks are separated by a blank line. Each block except for the last one must begin with a line of the form:


package: package-name

This may be followed by a line of the form

  

Depends: package-name1|package-name2,...

and/or a line of the form:

  

Conflicts: package-name1,...

The last line of the file has the form:

  

Install: package-name1,...

Spaces between package names are allowed and should be ignored. For example, the following snippets should be treated the same:

  

Depends:a,b,c

Depends : a,   b, c  

The meaning of each block is a definition of dependencies:

  

The described package is the one listed right after package:  in the first line of the block.

The list after Depends:  is a list of packages that need to be installed in order to install the described package. A comma means "and", a pipe means "or".

The list after Conflicts:  is a list of packages that conflict with the described package -- they are not allowed to be installed if we want to install the package.

The meaning of the last line of the file is just a list of packages that we want to install.

  

For example, the file benchmarks/ex1.dep describes a scenario in which we would like to install apache. This package requires either java or c, and also requires either apt or c. It conflicts with the package spring. The package java depends on both c and apt. The package apt depends on spring.

  

The program you are implementing should either output There is no installation plan or There is an installation plan. In the latter case, starting from the second line of the output, the installation plan should be printed, each package in its own line.

  

### Examples

This repository contains some example dep files. Below is the expected results for these files:

  
```
$ python3 install_bool.py benchmarks/ex1.dep

There is an installation plan:

apache

c

  

$ python3 install_bool.py benchmarks/ex2.dep

There is no installation plan

  

$ python3 install_bool.py benchmarks/ex3.dep

There is an installation plan:

apt

java

apache

  

$ python3 install_bool.py benchmarks/ex4.dep

There is no installation plan
```

Important note: it is OK if your implementation suggests a different installation plan.

  
  
  

## Solution.

Given a package A, let's assume its 
Dependencies are : G, B, C|D
And Conflict: E,F

For each package we will create variable.

To calculate its possible installation plan, we add package A itself to the general formula, along with two more expressions:


1. Dependencies

$A \implies (G\land B\land (C\lor D))$

2. Conflicts

$A \implies (\lnot E \land \lnot F)$

  

If we install package A, since A itself is added to the formula, ensuring A has a True value, the formula $A \implies (G\land B\land (C\lor D))$ will be satisfiable only if $(G\land B\land (C\lor D))$ is satisfied. Similarly, we must also satisfy $(\lnot E \land \lnot F)$.

For each package encountered in our installation plan for the target packages, we will recursively create two expressions and form a general formula.

> [!NOTE]
> 
> 1. We add only target packages to the formula as clauses with single literals. This means that if we need to install packages A and B, we will add them to the formula as $A\land B\land \ldots$ to ensure they result in a True value. However, we will not do the same for other packages, even if they are dependencies of A or B.
> 2. We iterate through all packages recursively using a queue. If a package is mentioned in the file but not in the "installation tree" of the target package, it might not appear in the formula.

In the end, we will use the pysmt solver to solve the formula. If there is an assignment that satisfies the formula, then every variable with a True value will be part of the installation plan, and variables with a False value will not.

### How to Run

You need to install the `pysmt` library and the `z3` solver for this exercise. You can find more information in their respective documentation




## How to run
You have to instal `pysmt` library and `z3` solver for this exercise. To can read about it more in there documentation.
[PySMT GitHub](https://github.com/pysmt/pysmt)