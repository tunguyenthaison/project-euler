# The sum of the primes below $10$ is $2 + 3 + 5 + 7 = 17$.
# Find the sum of all the primes below two million.

import time

def sum_prime(n: int) -> int:
    # sum of all prime numbers less than or equal to n
    
    if n == 1:
        return 0
    elif n == 2:
        return 2 
    else:
        list_primes = [2, 3]
        sum_result = 5
        x = list_primes[-1]
        while x + 2 <= n:
            x += 2
            # check if x is a prime by dividing x by primes numbers in the list
            flag = 1 # default the number is prime
            for p in list_primes:
                if  p * p > x :
                    break
                elif x % p == 0:
                    flag = 0 # not a prime, break
                    break
            if flag == 1:    
                # print(f'{x} is a prime')
                list_primes.append(x) # is a prime, add to list
                sum_result += x
            # print(list_primes)
            # print('---------------')
    # print(list_primes)
    return sum_result

if __name__ == "__main__":
    n = 2*1000000

    start_time = time.time()
    print(sum_prime(n))
    print(time.time() - start_time)
