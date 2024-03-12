# A palindromic number reads the same both ways. The largest palindrome made 
# from the product of two -digit numbers is 9009=91*99.
# Find the largest palindrome made from the product of 3-digit numbers.


def is_palindrome(n: int) -> bool:
    digits = []
    numb = n
    while numb > 0:
        x = numb % 10
        numb = (numb - x) // 10
        digits.append(x)
    return digits == digits[::-1]


def largest_palindrome_product(n_digit: int) -> list[int]:    
    max_numb = 1
    for i in range(n_digit):
        max_numb *= 10
    max_numb -= 1
    max_palindrome = 0
    for x in range(max_numb, 99, -1):
        for y in range(x, 99, -1):
            n = x*y
            if is_palindrome(n) and n > max_palindrome:
                max_palindrome = n
    return max_palindrome

if __name__ == "__main__":
    print(largest_palindrome_product(3))
