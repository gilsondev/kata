import pytest

"""
Program: Fizz Buzz

1. Divisible by 3 = Fizz
2. Divisible by 5 = Buzz
3. Divisible by 3 and 5 = FizzBuzz

"""

MIN = 1
MAX = 104

def fizzbuzz(number):
    result = []

    if MIN <= number <= MAX:
        for num in range(1, (number + 1)):
            is_divisible_by_3 = (num % 3) == 0
            is_divisible_by_5 = (num % 5) == 0
            divisible = [is_divisible_by_3, is_divisible_by_5]

            match divisible:
                case [True, True]:
                    result.append("FizzBuzz")
                case [True, False]:
                    result.append("Fizz")
                case [False, True]:
                    result.append("Buzz")
                case _:
                    result.append(str(num))

    return result


def test_divisible_by_3():
    assert fizzbuzz(3) == ["1", "2", "Fizz"]


def test_divisible_by_5():
    assert fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]


def test_divisible_by_3_and_5():
    assert fizzbuzz(15) == [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz",
    ]

def test_invalid_value_fizzbuzz():
    assert fizzbuzz(0) == []
    assert fizzbuzz(105) == []


if __name__ == "__main__":
    pytest.main(["-svv", __file__])
