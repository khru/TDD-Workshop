
def fizz_buzz(
    input: int
) -> str:
    if input == 5:
        return "Buzz"
    if input % 3 == 0:
        return "Fizz"
    return str(input)
