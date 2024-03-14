import time

def prime_number(n: int) -> int:

    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        list_primes = [2, 3]
        x = list_primes[-1]
        while len(list_primes) < n:
            x += 2
            # check if x is a prime by dividing x by primes numbers in the list
            flag = 1 # flag = 0 to default the number is prime
            for p in list_primes:
                if  p * p > x :
                    break
                elif x % p == 0:
                    flag = 0 # not a prime, break
                    break
            if flag == 1:    
                # print(f'{x} is a prime')
                list_primes.append(x) # is a prime, add to list

    return list_primes[-1]
        
        

if __name__ == "__main__":
    n = 10001

    start_time = time.time()
    print(prime_number(n))
    print(time.time() - start_time)

    