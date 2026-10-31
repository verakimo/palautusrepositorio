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
