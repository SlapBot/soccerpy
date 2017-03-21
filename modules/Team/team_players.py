from soccerpy.modules.Fundamentals.players import Players


class TeamPlayers:
    def __init__(self, data, headers):
        self.headers = headers
        self.links = Links(data['_links'])
        self.count = data['count']
        self.players = Players(data['players'])


class Links:
    def __init__(self, links):
        self.url = links['self']['href']
        self.team = links['team']['href']
