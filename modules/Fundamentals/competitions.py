from soccerpy.modules.Competition.competition import Competition as Parent
from soccerpy.modules.Fundamentals.searchable import Searchable
from collections.abc import Sequence


class Competitions(Searchable, Sequence):
    def __len__(self):
        return len(self.competitions)

    def __getitem__(self, index):
        return self.competitions[index]

    def __init__(self, data):
        super(Competitions, self).__init__()
        self.data = data
        self.competitions = []
        self.process()

    def process(self):
        for competition in self.data:
            self.competitions.append(Competition(competition))

    def explicit_search(self, competitions, query, searching_parameter="name"):
        if searching_parameter.lower() == "name":
            status = self.finder.search_for_competition_by_name(competitions, query=query)
        else:
            status = self.finder.search_for_competition_by_code(competitions, query=query)
        if status:
            return status
        return "Not Found"

    def search_by_name(self, query):
        dataset = self.competitions
        return self.explicit_search(dataset, query=query, searching_parameter="name")

    def search_by_code(self, query):
        dataset = self.competitions
        return self.explicit_search(dataset, query=query, searching_parameter="code")


class Competition:
    def __init__(self, competition):
        self.links = Links(competition['_links'])
        self.id = competition['id']
        self.caption = competition['caption']
        self.league = competition['league']
        self.year = competition['year']
        self.current_matchday = competition['currentMatchday']
        self.number_of_matchdays = competition['numberOfMatchdays']
        self.number_of_teams = competition['numberOfTeams']
        self.number_of_games = competition['numberOfGames']
        self.last_updated = competition['lastUpdated']
        self.parent = Parent()

    def get(self):
        return self.parent.get_specific(self.id)

    def get_teams(self):
        return self.parent.get_teams(self.id)

    def get_fixtures(self, matchday=None, time_frame=None):
        return self.parent.get_fixtures(self.id, matchday=matchday,
                                        time_frame=time_frame)

    def get_league_table(self, matchday=None):
        return self.parent.get_league_table(self.id, matchday=matchday)


class Links:
    def __init__(self, links):
        self.url = links['self']['href']
        self.teams = links['teams']['href']
        self.fixtures = links['fixtures']['href']
        self.league_table = links['leagueTable']['href']
