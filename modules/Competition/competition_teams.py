from soccerpy.modules.Fundamentals.links.competition_links import CompetitionLinks
from soccerpy.modules.Fundamentals.teams import Teams


class CompetitionTeams:
    def __init__(self, data, headers):
        self.headers = headers
        self.links = CompetitionLinks(data["_links"])
        self.count = data['count']
        self.teams = Teams(data['teams'])
