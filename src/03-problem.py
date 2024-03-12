# Largest Prime Factor
# https://projecteuler.net/problem=3

import numpy as np

def is_prime(numb: int) -> bool:
    x = int(np.floor(np.sqrt(numb)))
    # print(f'test {x}')
    for n in range(2, x+1):
        print(n)
        if numb % n == 0:
            return False 
    return True

def largest_prime(numb: int) -> int:
    n = numb
    x = int(np.floor(np.sqrt(n)))
    for i in range(1, x, 1):
        print(f'testing{i}')
        if n % i == 0:
            n = n // i
            if is_prime(n):
                return n
            
                




if __name__ == "__main__":
    numb = 600851475143
    # numb = 97
    print(f'The largest prime factor of {numb} is {largest_prime(numb)}')
    # print(is_prime(25))