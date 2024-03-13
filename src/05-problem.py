from timeit import default_timer as timer
import numpy as np



def eratosthenes(n: int) -> int:
    full_list = list(range(2, n+1, 1))
    divisor = 2
    while divisor * divisor <= n:

        # getting the nonzero elements (not divisible `by divisor`)
        numb_nonzero = [x if (x == divisor or x % divisor!= 0) else 0 for x in full_list]

        # getting the nonzero INDEX of nonzero elements (not divisible `by divisor`)
        ind_nonzero = [i for i, x in enumerate(numb_nonzero) if x != 0]

        # update the list to select only those nonzero elements
        full_list = [full_list[i] for i in ind_nonzero]

        # increase the divisor
        divisor += 1

    return full_list
    
def gcd(a: int, b: int) -> int:
    # find the greatest common divisor of two integers a, b
    r = b % a 
    while r > 0:
        b = a
        a = r 
        r = b % a 
    return a 


def smallest_multiple(n: int) -> int:
    
    # getting the list of all primes <= n
    list_primes = eratosthenes(n)
    
    # finding the product `numb` of all such primes <= n
    numb = 1
    for x in list_primes:
        numb *= x

    # loop from 1 to n, for the number `x` that is not in the primes list yet,
    # we find the `temp_gcd`: common greatest divisor with numb, then update
    # numb = numb * (x // temp_gcd)
    for x in range(1, n + 1, 1):
        if x not in list_primes and numb % x != 0:
                temp_gcd = gcd(x, numb)
                numb = numb * (x // temp_gcd)
    return numb
            


if __name__ == "__main__":
    start = timer() 
    print(smallest_multiple(5000))
    end = timer()
    print(end - start)    
    
    