from soccerpy.modules.Fundamentals.players import Players
from soccerpy.modules.Fundamentals.links.team_links import TeamLinks


class TeamPlayers:
    def __init__(self, data, headers):
        self.headers = headers
        self.links = TeamLinks(data['_links'])
        self.count = data['count']
        self.players = Players(data['players'])
