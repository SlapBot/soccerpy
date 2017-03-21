from collections.abc import Sequence


class Players(Sequence):
    def __len__(self):
        return len(self.players)

    def __getitem__(self, index):
        return self.players[index]

    def __init__(self, data):
        self.data = data
        self.players = []
        self.process()

    def process(self):
        for player in self.data:
            self.players.append(Player(player))


class Player:
    def __init__(self, player):
        self.name = player['name']
        self.position = player['position']
        self.jersey_number = player['jerseyNumber']
        self.dateOfBirth = player['dateOfBirth']
        self.nationality = player['nationality']
        self.contract_until = player['contractUntil']
        self.market_value = player['marketValue']
