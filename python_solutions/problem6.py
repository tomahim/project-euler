from python_solutions.utils import timing


@timing
def get_squares_of_sum_difference_with_sum_of_squares_naive(limit: int):
    num_range = range(1, limit + 1)
    return sum(num_range) ** 2 - sum(a ** 2 for a in num_range)


@timing
def get_squares_of_sum_difference_with_sum_of_squares_optimized(limit: int):
    sum_ = (limit * (limit + 1)) / 2
    sum_square = ((2 * limit + 1) * (limit + 1) * limit) / 6
    return sum_ ** 2 - sum_square


if __name__ == '__main__':
    """
    The sum of the squares of the first ten natural numbers is,

    1² + 2² + ... + 10² = 385
    The square of the sum of the first ten natural numbers is,
    
    (1 + 2 + ... + 10)² = 552 = 3025
    Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
    
    Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
    """

    limit = 10
    example_answer = 2640

    assert example_answer == get_squares_of_sum_difference_with_sum_of_squares_naive(limit)

    limit = 100
    result = get_squares_of_sum_difference_with_sum_of_squares_naive(limit)

    print(f'Response is : {result}')

    limit = 10
    assert example_answer == get_squares_of_sum_difference_with_sum_of_squares_optimized(limit)

    limit = 100
    result = get_squares_of_sum_difference_with_sum_of_squares_optimized(limit)

    print(f'Response is : {result}')
