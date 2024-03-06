
def sum_multiples_3_5(numb: int) -> int:
    # this is a brute-force solution
    sum = 0
    for x in range(1, numb, 1):
        if (x % 3 == 0 or x % 5 == 0):
            sum+=x 
    return sum

if __name__ == "__main__":
    numb = 1000
    # this is a brute-force solution
    print(f'Sum of multiples of 3 or 5 under {numb} is: {sum_multiples_3_5(numb)}')
