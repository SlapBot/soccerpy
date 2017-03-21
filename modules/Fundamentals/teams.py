from soccerpy.modules.Team.team import Team as Parent
from collections.abc import Sequence


class Teams(Sequence):
    def __len__(self):
        return len(self.teams)

    def __getitem__(self, index):
        return self.teams[index]

    def __init__(self, data):
        self.data = data
        self.teams = []
        self.handle()

    def handle(self):
        for team in self.data:
            self.teams.append(Team(team))


class Team:
    def __init__(self, team):
        self.links = TeamLinks(team['_links'])
        self.id = int(self.links.url.split("/")[-1])
        self.name = team['name']
        self.code = team['code']
        self.short_name = team['shortName']
        self.squad_market_value = team['squadMarketValue']
        self.crest_url = team['crestUrl']
        self.parent = Parent()

    def get(self):
        return self.parent.get(self.id)

    def fixtures(self):
        return self.parent.get_fixtures(self.id, season=None, time_frame=None, venue=None)

    def players(self):
        return self.parent.get_players(self.id)


class TeamLinks:
    def __init__(self, links):
        self.url = links['self']['href']
        self.fixtures = links['fixtures']['href']
        self.players = links['players']['href']
