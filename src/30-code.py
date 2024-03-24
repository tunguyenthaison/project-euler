import math

def digit_5_powers():
    # condition for an n-dinits number x 
    # 10^n <= 9^5 * (n+1)
    n = 1
    while math.pow(10, n) <= math.pow(9, 5) * (n + 1):
        n += 1
    print(f'n={n}') # n = 6
    # find x such that x = ... and x <= 9^5*7
    min_number = int(math.pow(10, 2))
    max_number = int(math.pow(9, 5) * (n + 1)) 
    all_sum = 0
    for x in range(min_number, max_number, 1):        
        arr = [int(digit) for digit in str(x)]
        x_fifth_power = 0
        for digit in arr:
            x_fifth_power += math.pow(digit, 5)    
        if x == x_fifth_power:
            all_sum += x 
    return all_sum


if __name__ == "__main__":
    print(digit_5_powers()) 