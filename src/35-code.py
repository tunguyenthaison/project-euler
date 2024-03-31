import math 
import time 

def is_prime(x: int) -> bool:
    if x == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(x)) + 1):
            # if i * i > x and x % i == 0:
            if x % i == 0:
                return False 
    return True

def array_circular(x: int) -> list[int]:
    str_x = str(x) 
    array_circular = []
    for i in range(0,len(str(x))):
        first = str_x[0:i]
        second = str_x[i:]
        temp = int(second+first)
        if is_prime(temp):
            array_circular.append(temp)
        else:
            return False
    return True

 
def circular_primes(n: int) -> int:
    # --->  loop 1 to n
    # check is it is a prime
    # if yes, do array_circula
    # check is prime for all in that array
    # count = 1
    new = []
    for i in range(2, n-1):
        if is_prime(i) and array_circular(i):
            new.append(i)
    return new 

# to solve optimally: we need to find a list of all primes < n
# loop in this list https://en.wikipedia.org/wiki/Eratosthenes

if __name__ == "__main__":
    n = 100
    # print(is_prime(n))
    # print(array_circular(n))
    start = time.time()
    print(len(circular_primes(n)))
    print(f'time = {time.time() - start}')
# start. list_primes = [2,3]
# 1. end = 3 + 2 = 5
   # check if 5 is divisible by any of the number in list_primes 