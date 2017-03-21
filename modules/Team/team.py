from soccerpy.modules.base_module import BaseModule


class Team(BaseModule):
    def __init__(self):
        super(Team, self).__init__()

    def get(self, team_id):
        data = self.r.request("team", endpoint_format=team_id)
        return TeamSpecific(data)

    def get_fixtures(self, team_id, season=None, time_frame=None, venue=None):
        data = self.r.request("team_fixtures", endpoint_format=team_id,
                              payload={"season": season,
                                       "timeFrame": time_frame,
                                       "venue": venue})
        return TeamFixtures(data)

    def get_players(self, team_id):
        data = self.r.request("team_players", endpoint_format=team_id)
        return TeamPlayers(data)