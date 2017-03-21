from soccerpy.modules.Competition.competition_fixtures import CompetitionFixtures
from soccerpy.modules.Competition.competition_league_table import CompetitionLeagueTable
from soccerpy.modules.Competition.competition_teams import CompetitionTeams
from soccerpy.modules.Competition.competitions_all import Competitions
from soccerpy.modules.base_module import BaseModule


class Competition(BaseModule):
    def __init__(self):
        super(Competition, self).__init__()

    def get(self, season=None, raw=False):
        data, headers = self.r.request('competitions', payload={"season": season})
        if raw:
            return data
        return Competitions(data, headers)

    def get_all(self):
        return self.get()

    def get_by_season(self, season):
        return self.get(season=season)

    def get_teams(self, competition_id, season=None):
        data, headers = self.r.request('competition_teams', endpoint_format=competition_id)
        return CompetitionTeams(data, headers)

    def get_league_table(self, competition_id, matchday=None, season=None):
        data, headers = self.r.request('competition_league_table', endpoint_format=competition_id,
                                       payload={'matchday': matchday})
        return CompetitionLeagueTable(data, headers)

    def get_league_table_by_matchday(self, competition_id, matchday):
        return self.get_league_table(competition_id, matchday=matchday)

    def get_fixtures(self, competition_id, matchday=None, time_frame=None, season=None):
        data, headers = self.r.request('competition_fixtures', endpoint_format=competition_id,
                                       payload={'matchday': matchday,
                                                'timeFrame': time_frame})
        return CompetitionFixtures(data, headers)

    def get_fixtures_by_matchday(self, competition_id, matchday):
        return self.get_fixtures(competition_id, matchday=matchday)

    def get_fixtures_by_time_frame(self, competition_id, time_frame):
        return self.get_fixtures(competition_id, time_frame=time_frame)

    def get_fixtures_by_matchday_and_time_frame(self, competition_id, matchday, time_frame):
        return self.get_fixtures(competition_id, matchday=matchday, time_frame=time_frame)


if __name__ == "__main__":
    c = Competition()
    comps = c.get_by_season(2015)
    print(comps)
    print(comps[0].league)
