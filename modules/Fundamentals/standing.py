from soccerpy.modules.Fundamentals.links.team_links import TeamLinks
from collections.abc import Sequence


class Standing(Sequence):
    def __len__(self):
        return len(self.teams)

    def __getitem__(self, index):
        return self.teams[index]

    def __init__(self, data):
        self.data = data
        self.teams = []
        self.process()

    def process(self):
        if isinstance(self.data, dict):
            self.teams = self.data
        else:
            for team in self.data:
                # noinspection PyUnresolvedReferences
                self.teams.append(Team(team))


class Team:
    def __init__(self, team):
        self.links = TeamLinks(team['link'])
        self.position = team['position']
        self.team_name = team['teamName']
        self.crest_url = team['crestURI']
        self.played_games = team['playedGames']
        self.points = team['points']
        self.goals = team['goals']
        self.goals_against = team['goalsAgainst']
        self.goal_difference = team['goalDifference']
        self.wins = team['wins']
        self.draws = team['draws']
        self.losses = team['losses']
        self.home = Location(team['home'])
        self.away = Location(team['away'])


class Location:
    def __init__(self, location):
        self.goals = location['goals']
        self.goals_against = location['goalsAgainst']
        self.wins = location['wins']
        self.draws = location['draws']
        self.loses = location['loses']
