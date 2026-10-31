class Player:
    def __init__(self, player_data):
        self.name = player_data['name']
        self.team = player_data['team']
        self.goals = player_data['goals']
        self.assists = player_data['assists']
        self.nationality = player_data['nationality']

    @property
    def points(self):
        return self.goals + self.assists

    def __str__(self):
        return f"{self.name:20} {self.team:15} {self.goals} + {self.assists} = {self.points}"
