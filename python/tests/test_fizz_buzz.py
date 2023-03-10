import pytest

from src.fizz_buzz import fizz_buzz


class TestFizzBuzz:

    @pytest.mark.parametrize("number, expected_result",
                             [(1, "1"),
                              (2, "2"),
                              (4, "4"),
                              (7, "7")
                              ])
    def test_given_a_number_than_is_not_divisible_by_3_or_5_we_get_the_same_number_as_a_str(
            self,
            number: int,
            expected_result: str,
    ):
        assert fizz_buzz(number) == expected_result

    @pytest.mark.parametrize("number, expected_result",
                             [(3, "Fizz"),
                              (6, "Fizz"),
                              (9, "Fizz"),
                              (12, "Fizz"),
                              ])
    def test_given_a_number_that_is_multiple_of_three_return_fizz(
            self,
            number: int,
            expected_result: str,
    ):
        assert fizz_buzz(number) == expected_result

    @pytest.mark.parametrize("number, expected_result",
                             [(5, "Buzz"),
                              (10, "Buzz"),
                              (20, "Buzz"),
                              ])
    def test_given_a_number_that_is_multiple_of_five_return_buzz(
            self,
            number: int,
            expected_result: str,
    ):
        assert fizz_buzz(number) == expected_result

    def test_given_a_15_then_return_fizzbuzz(self):
        assert fizz_buzz(15) == "FizzBuzz"

    def test_given_a_30_then_return_fizzbuzz(self):
        assert fizz_buzz(30) == "FizzBuzz"

    #def test_given_a_number_that_is_multiple_of_three_and_five_return_fizzbuzz(

