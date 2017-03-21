from collections.abc import Sequence


class CompetitionTeams:
    def __init__(self, data):
        self.links = Links(data["_links"])
        self.count = data['count']
        self.teams = Teams(data['teams'])


class Links:
    def __init__(self, links):
        self.url = links['self']['href']
        self.competition = links['competition']['href']


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
        self.team_links = TeamLinks(team['_links'])
        self.name = team['name']
        self.code = team['code']
        self.short_name = team['shortName']
        self.squad_market_value = team['squadMarketValue']
        self.crest_url = team['crestUrl']


class TeamLinks:
    def __init__(self, links):
        self.url = links['self']['href']
        self.fixtures = links['fixtures']['href']
        self.players = links['players']['href']
