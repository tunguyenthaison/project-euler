

A Pythagorean triplet is a set of three natural numbers, $a \lt b \lt c$, for which,
$$a^2 + b^2 = c^2.$$

For example, $3^2 + 4^2 = 9 + 16 = 25 = 5^2$.

There exists exactly one Pythagorean triplet for which $a + b + c = 1000$.<br>Find the product $abc$.

---

Here $n=1000$.

We write 

$$
\begin{aligned}
    (a+b)^2 &= (n - c)^2 \qquad \Longrightarrow\qquad 2ab+2nc = n^2 \\
    a^2 + 2ab + b^2 &= n^2 -2nc + c^2
\end{aligned}
$$

Therefore

$$
    ab = kn \qquad\text{for some}\; k \;\text{integer}.
$$

Furthermore we see that $n$ must be divisible by $2$, and

$$
    k + c = \frac{n}{2}. 
$$

Therefore

$$
    a+b = n - c = n - \left(\frac{n}{2}-k\right) = \frac{n}{2} - k. 
$$

Hence

$$
\begin{cases}
\begin{aligned}
    a + b &=  \frac{n}{2} - k \\
    a b   &= nk. 
\end{aligned}
\end{cases}
$$  

We only need to run an $\mathcal{O}(1)$-algorithm, using the quadratic formula, to check if there is an integer solution.

$$
    x^2 - Bx + C = 0.
$$

Back to the problem, we loop over $k$, thus this is an $\mathcal{O}(n)$ solution.