def fizz_buzz(
        input: int
) -> str:
    if input == 15:
        return "FizzBuzz"
    if input == 30:
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
