import requests

from player import Player


class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_player_data(self):
        return requests.get(self.url, timeout=10).json()

    def get_players(self):
        return [Player(player_dict) for player_dict in self.get_player_data()]
