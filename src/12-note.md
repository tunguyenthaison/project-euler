# [12. Highly Divisible Triangular Number](https://projecteuler.net/problem=12)

## Problem

For a given $n$ as the index, the $n^{th}$-triangle number is
$$
    T_n = \frac{n(n+1)}{2}.
$$
Let $\mathcal{D}(m) = \{x\in \mathbb{N}: m\;\text{is divisible by}\;x \;\text{and}\;1\leq x\leq n\}$. Then 
$$
    \mathfrak{D}(m) = |\mathcal{D}(m)|
$$ 
is the number of divisors of $m$.
For example:


<div align="center">

|$n$   | $T_n$    |$\mathfrak{D}(T_n)$|      $\mathcal{D}(T_nn)$ |
|:---: | :---:    |    :---:          |          :---            |
| 1    | 1        |1                  |$\{1\}$                   |
| 2    | 3        |2                  |$\{1,3\}$                 | 
| 3    | 6        |4                  |$\{1,2,3,4\}$             | 
| 4    | 10       |4                  |$\{1,2,5,10\}$            |
| 5    | 15       |4                  |$\{1,3,5,15\}$            |
| 6    | 21       |4                  |$\{1,3,7,21\}$            |
| 7    | 28       |6                  |$\{1,2,4,7,14, 28\}$      |

</div>

The question is, given $n$, finding the first $T_k$ such that $\mathfrak{D}(T_k) > n$.


## Anaysis

- We can write the $\mathfrak{D}(m)$ as `counting_divisor(n)` function that has complexity $\mathcal{O}(m^{1/2})$ by brute-force. 
- The next step is, we run an index $i=1,2,\ldots$, for each step:
  + $T_i= \frac{i(i+1)}{2}$, this costs $\mathcal{O}(1)$.
  + Check if $\mathfrak{D}(T_i) > n$, this costs $\mathcal{O}(|T_i|^{1/2})\sim \mathcal{O}(i)$.
  + Stop at the first $i = k$ such that $\mathfrak{D}(T_{k}) > n$. 
- The total complexity will be 
  $$
    \sum_{i=1}^k \mathcal{O}(i) \sim \mathcal{O}\left(k^2\right).
  $$

- The question is: how to estimate $k$ in terms of $n$?