from collections.abc import Sequence


class CompetitionFixtures:
    def __init__(self, data):
        self.links = Links(data['_links'])
        self.count = data['count']
        self.fixtures = Fixtures(data['fixtures'])


class Links:
    def __init__(self, links):
        self.url = links['self']['href']
        self.competition = links['competition']['href']


class Fixtures(Sequence):
    def __len__(self):
        return len(self.fixtures)

    def __getitem__(self, index):
        return self.fixtures[index]

    def __init__(self, data):
        self.data = data
        self.fixtures = []
        self.process()

    def process(self):
        for fixture in self.data:
            self.fixtures.append(Fixture(fixture))


class Fixture:
    def __init__(self, fixture):
        self.links = FixtureLinks(fixture['_links'])
        self.date = fixture['date']
        self.status = fixture['status']
        self.matchday = fixture['matchday']
        self.home_team_name = fixture['homeTeamName']
        self.away_team_name = fixture['awayTeamName']
        self.result = Result(fixture['result'])
        self.odds = fixture['odds']


class FixtureLinks:
    def __init__(self, links):
        self.url = links['url']['href']
        self.competition = links['competition']['href']
        self.home_team = links['homeTeam']['href']
        self.away_team = links['awayTeam']['href']


class Result:
    def __init__(self, result):
        self.goals_home_team = result['goalsHomeTeam']
        self.goals_away_team = result['goalsAwayTeam']
        if 'halfTime' in result:
            self.half_time = HalfTime(result['halfTime'])
        if 'extraTime' in result:
            self.extra_time = ExtraTime(result['extraTime'])
        if 'penaltyShootout' in result:
            self.penalty_shootout = PenaltyShootout(result['penaltyShootout'])


class HalfTime:
    def __init__(self, result):
        self.goals_home_team = result['goalsHomeTeam']
        self.goals_away_team = result['goalsAwayTeam']


class ExtraTime:
    def __init__(self, result):
        self.goals_home_team = result['goalsHomeTeam']
        self.goals_away_team = result['goalsAwayTeam']


class PenaltyShootout:
    def __init__(self, result):
        self.goals_home_team = result['goalsHomeTeam']
        self.goals_away_team = result['goalsAwayTeam']