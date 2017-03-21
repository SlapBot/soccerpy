from soccerpy.modules.Fundamentals.competitions import Competition


class CompetitionSpecific:
    def __init__(self, data, headers):
        self.headers = headers
        self.competition = Competition(data)
