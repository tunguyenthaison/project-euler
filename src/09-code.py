import time

def check_int_sol_quadratic(B: int, C: int):
    # check if x^2 - Bx + C = 0 
    # has two distinct integer solutions
    for x1 in range(1, B, 1):
        if C % x1 == 0:
            x2 = C // x1 
            if x1 + x2 == B:
                return [x1, x2]
    return None


def pythagorean_triplet(n: int) -> list[int]:
    # ab = n * k
    for k in range(2, n // 2, 1):
        c = (n // 2) - k
        # look for a^2 + b^2 = c^2 
        # THEN 
        # (1) a + b = k + n // 2
        # (2) a * b = n * k
        # THUS a, b are solutions to x^2 - (k + n//2)x + nk = 0
        B = k + n // 2
        C = n * k
        ans = check_int_sol_quadratic(B, C)
        if ans != None:
            a, b = ans[0], ans[1]
            return [a, b, c]
    return None


if __name__ == "__main__":
    n = 100000
    start_time = time.time()

    ans = pythagorean_triplet(n)
    if ans != None:
        print(f'a,b,c = {ans}')
        product = ans[0] * ans[1] * ans[2]

    print(product)
    
    print(time.time() - start_time)
