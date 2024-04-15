# Triangular, Pentagonal, and Hexagonal

import math

def solve_quadratic(A:int, B: int, C: int):
    # Ax^2 + Bx + C = 0
    # D = B^2 - 4AC
    # print(A, B, C)
    delta = B*B - 4*A*C 
    # print(f'delta = {delta}')

    if delta >= 0:
        sqrt_delta = int(math.sqrt(delta))
        if sqrt_delta ** 2 != delta:
            return None
        x1 = (-B +  math.sqrt(delta))/(2*A)
        # x2 = (-B -  math.sqrt(delta))/(2*A)
        # print(x1, x2)
        # return x1, x2 
        if x1//1 == x1:
            return int(x1)
        else:
            return None
    else:
        # if delta < 0, no solution
        return None

def check_T(x: int) -> int:
    # solve n*(n+1)/2 = x
    # n^2 + n - 2x = 0
    # pick the positive only
    T = solve_quadratic(1, 1, -2*x)
    return T

def check_P(x: int) -> int:
    # solve n*(3n-1)/2 = x
    # 3n^2 - n - 2x = 0
    # pick the positive only
    P = solve_quadratic(3, -1, -2*x)
    return P

def check_H(x: int) -> int:
    # solve n*(2n-1) = x
    # 2n^2 - n - x = 0
    # pick the positive only
    H = solve_quadratic(2, -1, -x)
    return H

def search_TPH() -> int:
    # solve, run for n in T as it is the smallest
    found = False
    n = 287
    while not found: 
        print(f'Loop of {n}')
        x = n * (n + 1) / 2
        checkP = check_P(x)
        checkH = check_H(x)

        if checkP and checkH:
            found = True
            print(checkP, checkH)
            print(not found)
        n += 1
    return n, checkP, checkH, x

 
if __name__ == "__main__":
    print(f"Welcome!")
    # x = 40755
    # print(check_T(x))
    # print(check_P(x))
    # print(check_H(x))
    print(search_TPH())