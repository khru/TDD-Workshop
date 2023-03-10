from src.fizz_buzz import fizz_buzz


class TestFizzBuzz:

    def test_given_a_1_we_expect_a_1(
            self,
    ):
        assert fizz_buzz(1) == "1"

    def test_given_a_2_we_expect_a_2(
            self,
    ):
        assert fizz_buzz(2) == "2"

    def test_given_a_4_we_expect_a_4(
            self,
    ):
        assert fizz_buzz(4) == "4"
