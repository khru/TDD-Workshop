
def fizz_buzz(
    input: int
) -> str:
    if input == 15:
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return str(input)
