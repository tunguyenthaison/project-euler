# [12. Highly Divisible Triangular Number](https://projecteuler.net/problem=12)

For a given $n$ as the index, the $n^{th}$-triangle number is
$$
    T_n = \frac{n(n+1)}{2}.
$$
Let $\mathcal{D}(n) = \{x\in \mathbb{N}: n\;\text{is divisible by}\;x \;\text{and}\;1\leq x\leq n\}$. Then 
$$
    \mathfrak{D}(n) = |\mathcal{D}(n)|
$$ 
is the number of divisors of $n$.
For example:


<div align="center">

|$n$   | $T_n$   |\mathfrak{D}(n)|      \mathcal{D}(n) |
|:---: | :---    |    :----      |          ---:       |
| 1    | 1       |1              |$\{1\}$              |
| 2    | 3       |2              |$\{1,3\}$            | 
| 3    | 6       |4              |$\{1,2,3,4\}$        | 
| 4    | 10      |4              |$\{1,2,5,10\}$       |
| 5    | 15      |4              |$\{1,3,5,15\}$       |
| 6    | 21      |4              |$\{1,3,7,21\}$       |
| 7    | 28      |6              |$\{1,2,4,7,14, 28\}$ |
