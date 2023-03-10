import pytest

from src.fizz_buzz import fizz_buzz


class TestFizzBuzz:

    @pytest.mark.parametrize("number, expected_result",
                             [(1, "1"),
                              (2, "2"),
                              (4, "4")
                              ])
    def test_given_a_number_than_is_not_divisible_by_3_or_5_we_get_the_same_number_as_a_str(
            self,
            number: int,
            expected_result: str,
    ):
        assert (fizz_buzz(number), expected_result)
