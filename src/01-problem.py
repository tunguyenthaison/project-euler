# from icecream import ic

def sum_multiples_3_5(numb: int) -> int:
    # this is a brute-force solution
    sum = 0
    for x in range(1, numb, 1):
        if (x % 3 == 0 or x % 5 == 0):
            sum+=x 
    return sum

def sum_multiples_3_5_upgrade(numb: int) -> int:
    # counting sum of 3k where 3k < numb
    k3 = (numb - 1) // 3
    # counting sum of 3k where 5k < numb
    k5 = (numb - 1) // 5
    # counting sum of 3k where 15k < numb
    k15 = (numb - 1) // 15
    # compute using #(A or B) = #A + #B - #(A and B)
    sum = 3*(k3 * (k3 + 1) // 2) + 5*(k5 * (k5 + 1) // 2) - 15*(k15 * (k15 + 1) // 2)
    return sum

if __name__ == "__main__":
    numb = 1000
    # this is a brute-force solution
    print(f'Sum of multiples of 3 or 5 under {numb} is: {sum_multiples_3_5(numb)}')
    print(f'Sum of multiples of 3 or 5 under {numb} is: {sum_multiples_3_5_upgrade(numb)}')
