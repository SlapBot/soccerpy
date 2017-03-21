from soccerpy.modules.Fundamentals.competitions import Competitions


class CompetitionsAll:
    def __init__(self, data, headers):
        self.headers = headers
        self.competitions = Competitions(data)
