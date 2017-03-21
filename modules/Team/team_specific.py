from soccerpy.modules.Fundamentals.teams import Team


class TeamSpecific:
    def __init__(self, data, headers):
        self.headers = headers
        self.team = Team(data)
