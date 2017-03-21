from collections.abc import Sequence


class AllCompetitions(Sequence):
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
            self.competitions.append(Competitions(competition))


class Competitions:
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


class Links:
    def __init__(self, links):
        self.url = links['self']['href']
        self.teams = links['teams']['href']
        self.fixtures = links['fixtures']['href']
        self.league_table = links['leagueTable']['href']
