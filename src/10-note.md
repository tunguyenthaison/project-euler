Project Euler 

# Problem 10
> The sum of the primes below $10$ is $2 + 3 + 5 + 7 = 17$. Find the sum of all the primes below two million.

---

## Solution

Given $n$, we first create a list of all prime numbers:
- [2,3].
- Loop from the end for the list, say $x=3$ to $x=x+2$.
- Check if this new number is divisible by any other member in the prime list, 
        * if yes, it is NOT a prime number, skip to the next `x+=2`
        * if no, it is a prime number, update the list and repeat. Add sum along the way.
  
## Complexity

- The outer loop is $\mathcal{O}(n)$.
- For each index of `x`, we loop through the length of the `prime_list`. Roughly speaking 
    we can say this list has length $\leq n$, thus the solution is of (less than or
    equal to) $\mathcal{O}(n^2)$. 

## Sharp complexity
Let $\pi(x)$ be the prime-counting function defined to be the number of primes less than or equal to $x$, for any real number $x$, then the [asymptotic law of distribution of prime numbers](https://en.wikipedia.org/wiki/Prime_number_theorem) says that [^1]:

$$
    \pi(x) \sim \frac{x}{\mathrm{log}\;x} \qquad\text{as}\qquad x\to +\infty.
$$

Using this, we have 

$$
    \text{complexity} \leq \mathcal{O}(n \times \pi(n)) \sim \mathcal{O}\left(\frac{n^2}{\log(n)}\right).
$$

It is a tiny bit better than $\mathcal{O}(n^2)$ but not really much.


[^1]: https://en.wikipedia.org/wiki/Prime_number_theorem