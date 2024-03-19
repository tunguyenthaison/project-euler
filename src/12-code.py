import math
import time

def count_divisors(n: int) -> int:
    """ Count the number of divisors for the integer n

    Args:
        n (int): the number n we want to count

    Returns:
        int: the number of divisors of the input
    """
    # O(n^(1/2)) algorithm, brute-force
    # if x is a divisor then n / x is also a divisor
    if n == 1:
        return 1
    else:
        count = 0
        for i in range(1, int(math.sqrt(n) + 1), 1):
            if n % i == 0:
                count += 1
        return count * 2

def highly_divisible_triangular_number(numb_divisors: int) -> int:
    # O(?)
    i = 1
    while count_divisors( i * (i + 1) // 2 ) <= numb_divisors:
        triangle_number = i * (i + 1) // 2
        # print(i, triangle_number, count_divisors(triangle_number))
        i += 1
    print(f'First index that have more than {numb_divisors} divisors is {i}')  
    return i * (i+1) // 2


if __name__ == "__main__":
    print("|---Problem 12---|")
    print("|----------------|")
    numb_divisors = 500

    start_time = time.time()
    print(f"The first triangle number that has more than {numb_divisors} is {highly_divisible_triangular_number(numb_divisors)}")
    print(time.time() - start_time)