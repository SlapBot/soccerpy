from soccerpy.modules.Fundamentals.teams import Teams


class CompetitionTeams:
    def __init__(self, data):
        self.links = Links(data["_links"])
        self.count = data['count']
        self.teams = Teams(data['teams'])


class Links:
    def __init__(self, links):
        self.url = links['self']['href']
        self.competition = links['competition']['href']
