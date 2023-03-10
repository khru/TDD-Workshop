from src.change_me import fizz_buzz


class TestFizzBuzz:

    def test_given_a_1_we_expect_a_1(
            self,
    ):
        assert fizz_buzz(1) == "1"
