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

## Some related ideas
Check [Divisor function - Wiki](https://en.wikipedia.org/wiki/Divisor_function), that the function we defined above is 

$$
    \sigma_0(m) = \mathfrak{D}(m) 
                = \text{the number of divisors of}\;m 
                = \sum_{d\,|\,m} d^0. 
$$

Furthermore, if 
$$
    m = \prod_{i=1}^r p_i^{a_i}
$$
where $p_i$'s are prime numbers, then 
$$
    \mathfrak{D}(m) = \sigma_0(m) = \prod_{i=1}^r (1+a_i).
$$

Or if we use [Growth-rate, Wikipedia](https://en.wikipedia.org/w/index.php?title=Euler%27s_totient_function&action=edit&section=16)

>In fact, during the proof of the second formula, the inequality
>$$
>{\displaystyle {\frac {6}{\pi ^{2}}}<{\frac {\varphi (n)\sigma (n)}{n^{2}}}<1,}
>$$
>true for n > 1, is proved.

Then 
$$
    \sigma(n) > \frac{6n^2}{\pi^2 \varphi(n)} > \frac{6n^2}{\pi^2 n} = Cn.
$$
Using $\varphi(n) > n$ using [Wiki](https://en.wikipedia.org/w/index.php?title=Euler%27s_totient_function&action=edit&section=16)

> First[29]
>$${\displaystyle \lim \sup {\frac {\varphi (n)}{n}}=1,}$$
> but as n goes to infinity,[30] for all $δ > 0$
>
Thus, in our algorithm: 
$$
    \sigma(k^2) > Ck^2 > n 
$$

is satisfied if $k> Cn^{1/2}$. The total complexity is thus 
$$
    \mathcal{O}(k^2) \sim \mathcal{O}(n).
$$
However it does not seem to be true, as the solution runs so slow still.
