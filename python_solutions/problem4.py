from python_solutions.utils import timing


def _is_palindrom(num: int):
    return str(num) == str(num)[::-1]


@timing
def find_largest_palindrome_from_product_of_two_n_digit_numbers(first_multiplier, max_multiplier, max_found=0):
    if first_multiplier <= max_multiplier - 9:
        return max_found

    for second_multiplier in reversed(range(0, first_multiplier)):
        num = first_multiplier * second_multiplier
        if _is_palindrom(num) and num > max_found:
            max_found = num

    return find_largest_palindrome_from_product_of_two_n_digit_numbers(first_multiplier-1, max_multiplier, max_found)


if __name__ == '__main__':
    """
    A palindromic number reads the same both ways. The largest palindrome made from the product 
    of two 2-digit numbers is 9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    example_answer = 9009

    assert example_answer == find_largest_palindrome_from_product_of_two_n_digit_numbers(99, 99)

    result = find_largest_palindrome_from_product_of_two_n_digit_numbers(999, 999)

    print(f'The largest palindrome made from the product of two 3-digit numbers is : {result}')
