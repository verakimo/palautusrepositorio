from player import Player
from player_stats import PlayerStats


class PlayerReaderStub:
    def get_players(self):
        return [
            Player({'name': 'Low', 'team': 'EDM', 'goals': 4, 'assists': 12, 'nationality': 'FIN'}),
            Player({'name': 'High', 'team': 'EDM', 'goals': 45, 'assists': 54, 'nationality': 'CAN'}),
            Player({'name': 'Other', 'team': 'PIT', 'goals': 37, 'assists': 53, 'nationality': 'FIN'}),
        ]


def test_top_scorers_by_nationality_filters_and_sorts():
    stats = PlayerStats(PlayerReaderStub())

    players = stats.top_scorers_by_nationality('FIN')

    assert [player.name for player in players] == ['Other', 'Low']


def test_top_scorers_by_team_filters_and_sorts():
    stats = PlayerStats(PlayerReaderStub())

    players = stats.top_scorers_by_team('EDM')

    assert [player.name for player in players] == ['High', 'Low']


def test_players_by_nationality_filters_players():
    stats = PlayerStats(PlayerReaderStub())

    players = stats.players_by_nationality('FIN')

    assert [player.name for player in players] == ['Low', 'Other']


def test_top_goal_scorers_sorts_and_limits_players():
    stats = PlayerStats(PlayerReaderStub())

    players = stats.top_goal_scorers(2)

    assert [player.name for player in players] == ['High', 'Other']
