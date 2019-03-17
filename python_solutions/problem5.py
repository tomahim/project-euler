from python_solutions.utils import timing


def _is_divisible(a, b):
    return a % b == 0


@timing
def get_smallest_number_evenly_divisible_by_range(num_range):
    max_value = max(num_range)
    current_value = max_value
    while True:
        if all(_is_divisible(current_value, denominator) for denominator in num_range[:-1]):
            break
        current_value += max_value
    return current_value


if __name__ == '__main__':
    """
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20 ?
    """
    example_range = range(1, 11)
    example_answer = 2520

    assert example_answer == get_smallest_number_evenly_divisible_by_range(example_range)

    result = get_smallest_number_evenly_divisible_by_range(range(1, 21))

    print(f'The smallest number evenly divisible by numbers between 1 and 20 : {result}')
