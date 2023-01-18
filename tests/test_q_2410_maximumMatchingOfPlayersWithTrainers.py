import pytest
from questions.q_2410_maximumMatchingOfPlayersWithTrainers import Solution


@pytest.mark.parametrize(
    "players, trainers, output", [([4, 7, 9], [8, 2, 5, 8], 2), ([1, 1, 1], [10], 1)]
)
class TestSolution:
    def test_matchPlayersAndTrainers(
        self, players: list[int], trainers: list[int], output: int
    ):
        sc = Solution()
        assert (
            sc.matchPlayersAndTrainers(
                players,
                trainers,
            )
            == output
        )
