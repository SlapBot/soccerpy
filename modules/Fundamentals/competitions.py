from soccerpy.modules.Competition.competition import Competition as Parent
from collections.abc import Sequence


class Competitions(Sequence):
    def __len__(self):
        return len(self.competitions)

    def __getitem__(self, index):
        return self.competitions[index]

    def __init__(self, data):
        self.data = data
        self.competitions = []
        self.process()

    def process(self):
        for competition in self.data:
            self.competitions.append(Competition(competition))


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

    def get_teams(self, season=None):
        return self.parent.get_teams(self.id, season=season)

    def get_fixtures(self, matchday=None, time_frame=None, season=None):
        return self.parent.get_fixtures(self.id, matchday=matchday,
                                        time_frame=time_frame, season=season)

    def get_league_table(self, matchday=None, season=None):
        return self.parent.get_league_table(self.id, matchday=matchday, season=season)


class Links:
    def __init__(self, links):
        self.url = links['self']['href']
        self.teams = links['teams']['href']
        self.fixtures = links['fixtures']['href']
        self.league_table = links['leagueTable']['href']
