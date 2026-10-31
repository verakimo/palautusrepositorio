from rich.console import Console
from rich.table import Table

from player_reader import PlayerReader
from player_stats import PlayerStats


def create_table(players, season, nationality):
    table = Table(title=f"Season {season} players from {nationality}")
    table.add_column("Player")
    table.add_column("Teams")
    table.add_column("Goals", justify="right")
    table.add_column("Assists", justify="right")
    table.add_column("Points", justify="right")

    for player in players:
        table.add_row(
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(player.points),
        )

    return table


def get_filtered_players(stats, filter_type, filter_value):
    if filter_type == "team":
        return stats.top_scorers_by_team(filter_value)
    return stats.top_scorers_by_nationality(filter_value)


def main():
    season = input("Season: ")
    filter_type = input("Filter by nationality or team: ")
    filter_value = input(f"{filter_type}: ")
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = get_filtered_players(stats, filter_type, filter_value)
    Console().print(create_table(players, season, filter_value))

if __name__ == "__main__":
    main()
