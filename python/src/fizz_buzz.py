def fizz_buzz(
        input: int
) -> str:
    if is_multiple_of_fifteen(input):
        return "FizzBuzz"
    if is_multiple_of_three(input):
        return "Fizz"
    if is_multiple_of_five(input):
        return "Buzz"
    return str(input)


def is_multiple_of_three(number: int) -> bool:
    return number % 3 == 0


def is_multiple_of_five(number: int) -> bool:
    return number % 5 == 0


def is_multiple_of_fifteen(number: int) -> bool:
    return number % 15 == 0
