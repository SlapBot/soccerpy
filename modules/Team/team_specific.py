from soccerpy.modules.Fundamentals.teams import Team


class TeamSpecific:
    def __init__(self, data):
        self.team = Team(data)
