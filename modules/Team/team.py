from soccerpy.modules.base_module import BaseModule
from soccerpy.modules.Team.team_specific import TeamSpecific
from soccerpy.modules.Team.team_fixtures import TeamFixtures
from soccerpy.modules.Team.team_players import TeamPlayers


class Team(BaseModule):
    def __init__(self):
        super(Team, self).__init__()

    def get(self, team_id):
        data, headers = self.r.request("team", endpoint_format=team_id)
        return TeamSpecific(data, headers)

    def get_fixtures(self, team_id, season=None, time_frame=None, venue=None):
        data, headers = self.r.request("team_fixtures", endpoint_format=team_id,
                                       payload={"season": season,
                                                "timeFrame": time_frame,
                                                "venue": venue})
        return TeamFixtures(data, headers)

    def get_fixtures_by_season(self, team_id, season):
        return self.get_fixtures(team_id, season=season)

    def get_fixtures_by_time_frame(self, team_id, time_frame):
        return self.get_fixtures(team_id, time_frame=time_frame)

    def get_fixtures_by_venue(self, team_id, venue):
        return self.get_fixtures(team_id, venue=venue)

    def get_fixtures_by_season_and_time_frame(self, team_id, season, time_frame):
        return self.get_fixtures(team_id, season=season, time_frame=time_frame)

    def get_fixtures_by_season_and_venue(self, team_id, season, venue):
        return self.get_fixtures(team_id, season=season, venue=venue)

    def get_fixtures_by_time_frame_and_venue(self, team_id, time_frame, venue):
        return self.get_fixtures(team_id, time_frame=time_frame, venue=venue)

    def get_players(self, team_id):
        data, headers = self.r.request("team_players", endpoint_format=team_id)
        return TeamPlayers(data, headers)
