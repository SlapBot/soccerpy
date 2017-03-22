from soccerpy.modules.Team.team import Team as Parent
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
