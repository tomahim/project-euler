import math

from python_solutions.utils import timing


@timing
def sum_multiples_3_and_5_naive(max):
    numbers = range(0, max)
    return sum([num for num in numbers if num % 3 == 0 or num % 5 == 0])


@timing
def sum_multiples_3_and_5_optimized(max):
    def sum_divisible_by(max, divisible_by):
        p = math.floor((max - 1) / divisible_by)
        return math.floor(divisible_by * (p * (p + 1)) / 2)


    return (
        sum_divisible_by(max, 3) +
        sum_divisible_by(max, 5) -
        sum_divisible_by(max, 15)
    )


if __name__ == '__main__':
    assert sum_multiples_3_and_5_naive(10) == 23

    expected_result = 233168

    assert sum_multiples_3_and_5_naive(1000) == expected_result

    assert sum_multiples_3_and_5_optimized(1000) == expected_result

    assert sum_multiples_3_and_5_naive(1000000) == sum_multiples_3_and_5_optimized(1000000)
