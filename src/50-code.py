from timeit import default_timer as timer

def eratosthenes(n: int) -> list[int]:
    """ Find the list of all primes less than or equal to n 
    
    Args:
        n (int): _description_

    Returns:
        list[int]: _description_
    """

    primes = list(range(1, n+1, 1))
    return primes

def consecutive_prime_sum(n: int) -> int: 
    if n == 2:
        return 2
    elif n == 3:
        return 5
    primes = [2,3]
    # sum = 5
    x = primes[-1]
    while x + 2 <= n:
        x += 2
        # check if x is a prime by dividing x by primes numbers in the list
        flag = 1 # flag = 0 to default the number is prime
        for p in primes:
            if  p * p > x :
                break
            elif x % p == 0:
                flag = 0 # not a prime, break
                break
        if flag == 1:    
            # print(f'{x} is a prime')
            primes.append(x) # is a prime, add to list
            # sum += x
    # print(f'primes = {primes}')
    answer = -1
    m = len(primes)
    for k in range(m, 0, -1):
        print(f'length k consider of {k} consecute')
        # for i in range(m - k, -1, -1):
        for i in range(0, m - k + 1, 1):
            # print(f'i = {i}')
            sum_length_k = sum(primes[i : i + k]) 
            if sum_length_k > n:
                break
            # print(f'sum {primes[i:i+k]} is {sum_length_k}')
            elif sum_length_k in primes:
                answer = sum_length_k
                # print(f'{sum_length_k} is a prime less than or equal to {n}')
                return answer, k, primes[i:i+k]
            # print('----')
    return None
                
    


if __name__ == "__main__":
    # print('Welcome to Project Euler #50.')
    n = 1000000
    # n = 100
    # print(eratosthenes(n))
    start = timer()
    print(f'The number is: {consecutive_prime_sum(n)}')
    end = timer()
    print(end - start) # Time in seconds, e.g. 5.38091952400282