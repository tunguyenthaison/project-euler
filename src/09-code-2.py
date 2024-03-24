import math

def solve_quadratic(A:int, B: int, C: int):
    # Ax^2 + Bx + C = 0
    # D = B^2 - 4AC
    print(A, B, C)
    delta = B*B - 4*A*C 
    print(f'delta = {delta}')
    if delta >= 0:
        x1 = (-B +  math.sqrt(delta))/(2*A)
        x2 = (-B -  math.sqrt(delta))/(2*A)
        print(x1, x2)
        return x1, x2 
    else:
        # if delta < 0, no solution
        return None
 
def eson(n: int) -> list[int]:
    # input n, return [a,b,c]
    for c in range(1, n, 1): 
        print(c)
        # solve for a,b such that
        # a + b = n - c = B 
        # a * b = n/2 * (n-c) = C
        # solve x^2 - Bx + C = 0
        A = 1
        B = n - c
        C = n * (n // 2 - c)
        if solve_quadratic(A, -B, C) is not None: 
            a, b = solve_quadratic(A, -B, C)
            print(a, b)
            # check a, b are integers?
            if a == int(a) and b == int(b):
                return [a, b, c]
        print('-----')
    return None


if __name__ == "__main__":
    n = 1000
    ans = eson(n)
    print(ans)
    # solve_quadratic(1,-4,4)
    