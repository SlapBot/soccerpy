from soccerpy.modules.Competition.competition_fixtures import Fixture, Fixtures


class FixturesSpecific:
    def __init__(self, data):
        self.fixture = Fixture(data['fixture'])
        self.head2head = Head2Head(data['head2head'])


class Head2Head:
    def __init__(self, head):
        self.count = head['count']
        self.time_frame_start = head['timeFrameStart']
        self.time_frame_emd = head['timeFrameEnd']
        self.home_team_wins = head['homeTeamWins']
        self.away_team_wins = head['awayTeamWins']
        self.draws = head['draws']
        self.last_home_win_home_team = Fixture(head['lastHomeWinHomeTeam'])
        self.last_win_home_team = Fixture(head['lastWinHomeTeam'])
        self.last_away_win_away_team = Fixture(head['lastAwayWinAwayTeam'])
        self.last_win_away_team = Fixture(head['lastWinAwayTeam'])
        self.fixtures = Fixtures(head['fixtures'])
