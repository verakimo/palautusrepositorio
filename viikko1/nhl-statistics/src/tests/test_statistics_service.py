import unittest

from player import Player
from statistics_service import SortBy, StatisticsService


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89),
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_finds_player(self):
        player = self.stats.search("Gretzky")

        self.assertEqual(player.name, "Gretzky")

    def test_search_returns_none_when_player_is_not_found(self):
        self.assertIsNone(self.stats.search("Unknown"))

    def test_team_returns_players_from_requested_team(self):
        players = self.stats.team("EDM")

        self.assertEqual(len(players), 3)
        self.assertTrue(all(player.team == "EDM" for player in players))

    def test_top_returns_players_in_points_order(self):
        players = self.stats.top(2)

        self.assertEqual(len(players), 2)
        self.assertEqual([player.name for player in players], ["Gretzky", "Lemieux"])

    def test_top_can_sort_by_goals(self):
        players = self.stats.top(2, SortBy.GOALS)

        self.assertEqual([player.name for player in players], ["Lemieux", "Yzerman"])

    def test_top_can_sort_by_assists(self):
        players = self.stats.top(2, SortBy.ASSISTS)

        self.assertEqual([player.name for player in players], ["Gretzky", "Yzerman"])


if __name__ == "__main__":
    unittest.main()
