from python_solutions.utils import timing


@timing
def compute_largest_prime_factor(value: int):
    denominator = 2
    while denominator < value:
        disivion_result = value / denominator
        if disivion_result.is_integer():
            value = disivion_result
        else:
            denominator += 1
    return value


if __name__ == '__main__':
    """
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?
    """
    example_value = 13195
    example_answer = 29

    assert example_answer == compute_largest_prime_factor(example_value)

    problem_value = 600851475143
    result = compute_largest_prime_factor(problem_value)

    print(f'Largest prime factor of {problem_value} is : {result}')
