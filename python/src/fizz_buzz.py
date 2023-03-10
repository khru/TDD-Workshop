def fizz_buzz(
        input: int
) -> str:
    fizzbuzz: dict = {
        15: "FizzBuzz",
        3: "Fizz",
        5: "Buzz",
    }
    for key in fizzbuzz:
        if input % key == 0:
            return fizzbuzz[key]

    return str(input)

