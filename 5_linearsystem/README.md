# Ordinary Differential Equations

## Introduction

There are many algorithms that can solve linear systems of the form ```A*x = b``` given the matrix ```A``` and the vector ```b```.
The [documentation](https://carlos-adir.github.io/NumericalMethods/5.html) explain better the methods and it's recomended to see it if you want understand about the methods.
There are two approachs to solve the systems:

1. Direct Methods
2. Iterative Techniques

The frist approach can give us the exact solution while the second approch gives us a better solution each time we iteract.

The frist approach is good when the system is small, and the computer's truncation error is very small, because the complexity of the solution is O(n^3).

The second approach is good when the system is very big and it's possible to estipulate an error, such as [fixed point](https://carlos-adir.github.io/NumericalMethods/1_2.html): we give a guess of ```x``` solution for the system, we iterate until the error is less than the tolerance.
The complexity of this approach is O(n^2) for each iteraction because it's just matrice multiplication.

## Files

All the methods to solve linear systems are implemented in the file ```methods.py```, the file ```inputs.py``` has examples of some linear systems with matrix ```A``` and vector ```b```.
The following files are the examples showing how to use each algorithm.

1. Direct Methods
    * Gaussian Elimination: ```1_gauss.py```
    * Partial Pivoting: ```2_partial.py```
    * Scaled Partial Pivoting: ```3_scaled.py```
    * LU decomposition: ```4_LU.py```
2. Iterative Techniques
    * Jacobi: ```5_jacobi.py```
    * Gauss-Seidel: ```6_gaussseidel.py```

Some examples in ```inputs.py``` give, purposely, the matrix ```A``` and the vector ```b``` not well conditioned which there is no solution, or even there is solution but the algorithm can not find a solution by its own limitation. 