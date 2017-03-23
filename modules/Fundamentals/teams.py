from soccerpy.modules.Fundamentals.master import Master
from soccerpy.modules.Fundamentals.searchable import Searchable
from collections.abc import Sequence


class Teams(Searchable, Sequence):
    def __len__(self):
        return len(self.teams)

    def __getitem__(self, index):
        return self.teams[index]

    def __init__(self, data):
        super(Teams, self).__init__()
        self.data = data
        self.teams = []
        self.handle()

    def handle(self):
        for team in self.data:
            self.teams.append(Team(team))

    def explicit_search(self, teams, query, searching_parameter="name"):
        if searching_parameter.lower() == "name":
            status = self.finder.search_for_team_by_name(teams, query=query)
        else:
            status = self.finder.search_for_team_by_code(teams, query=query)
        if status:
            return status
        return "Not Found"

    def search_by_name(self, query):
        dataset = self.teams
        return self.explicit_search(dataset, query=query, searching_parameter="name")

    def search_by_code(self, query):
        dataset = self.teams
        return self.explicit_search(dataset, query=query, searching_parameter="code")


class Team(Master):
    def __init__(self, team):
        super(Team, self).__init__()
        self.links = TeamLinks(team['_links'])
        self.id = int(self.links.url.split("/")[-1])
        self.name = team['name']
        self.code = team['code']
        self.short_name = team['shortName']
        self.squad_market_value = team['squadMarketValue']
        self.crest_url = team['crestUrl']

    def get(self):
        data, headers = self.r.request(raw_url=self.links.url)
        return Team(data)

    def fixtures(self):
        from soccerpy.modules.Fixture.fixtures_all import FixturesAll
        data, headers = self.r.request(raw_url=self.links.fixtures)
        return FixturesAll(data, headers)

    def players(self):
        from soccerpy.modules.Team.team_players import TeamPlayers
        data, headers = self.r.request(raw_url=self.links.players)
        return TeamPlayers(data, headers)


class TeamLinks:
    def __init__(self, links):
        self.url = links['self']['href']
        self.fixtures = links['fixtures']['href']
        self.players = links['players']['href']
