import pytest
from questions.q_0007_reverseInteger import Solution


@pytest.mark.parametrize("x, output", [(123, 321), (-123, -321), (120, 21)])
class TestSolution:
    def test_reverse(self, x: int, output: int):
        sc = Solution()
        assert (
            sc.reverse(
                x,
            )
            == output
        )

    def test_reverse_bitwise_operation(self, x: int, output: int):
        sc = Solution()
        assert (
            sc.reverse_bitwise_operation(
                x,
            )
            == output
        )
