from collections.abc import Sequence
from soccerpy.modules.Fixture.fixture import Fixture as Parent
from soccerpy.modules.Fundamentals.master import Master
from soccerpy.modules.Team.team_specific import TeamSpecific
from soccerpy.modules.Competition.competition_specific import CompetitionSpecific


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


class Fixture(Master):
    def __init__(self, fixture):
        super(Fixture, self).__init__()
        self.links = FixtureLinks(fixture['_links'])
        self.id = int(self.links.url.split("/")[-1])
        self.date = fixture['date']
        self.status = fixture['status']
        self.matchday = fixture['matchday']
        self.home_team_name = fixture['homeTeamName']
        self.away_team_name = fixture['awayTeamName']
        self.result = Result(fixture['result'])
        if fixture['odds']:
            self.odds = Odds(fixture['odds'])
        self.odds = Odds(fixture['odds'])
        self.parent = Parent()

    def get(self, head2head):
        return self.parent.get_specific(self.id, head2head=head2head)

    def competition(self):
        data, headers = self.r.request(raw_url=self.links.competition)
        return CompetitionSpecific(data, headers)

    def home_team(self):
        data, headers = self.r.request(raw_url=self.links.home_team)
        return TeamSpecific(data, headers)

    def away_team(self):
        data, headers = self.r.request(raw_url=self.links.away_team)
        return TeamSpecific(data, headers)


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


class Odds:
    def __init__(self, bets):
        self.home_win = bets['homeWin']
        self.draw = bets['draw']
        self.away_win = bets['awayWin']
