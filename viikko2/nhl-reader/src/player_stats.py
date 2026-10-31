class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()

    def players_by_nationality(self, nationality):
        return [player for player in self.players if player.nationality == nationality]

    def top_scorers_by_nationality(self, nationality):
        return sorted(
            self.players_by_nationality(nationality),
            key=lambda player: player.points,
            reverse=True,
        )

    def top_goal_scorers(self, how_many):
        """Return the top players by goals."""
        return sorted(
            self.players,
            key=lambda player: player.goals,
            reverse=True,
        )[:how_many]

    def top_scorers_by_team(self, team):
        players = [player for player in self.players if team in player.team.split(", ")]
        return sorted(players, key=lambda player: player.points, reverse=True)
