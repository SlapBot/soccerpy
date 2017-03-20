from soccerpy.modules.all_competitions import AllCompetitions
from soccerpy.modules.base_module import BaseModule


class Competition(BaseModule):
    def __init__(self):
        super(Competition, self).__init__()

    def get_competitions(self, season=None, raw=False):
        if season:
            data = self.r.request('competitions', payload={"season": season})
        else:
            data = self.r.request("competitions")
        if raw:
            return data
        return AllCompetitions(data)

    def get_all_competitions(self):
        return self.get_competitions()

    def get_all_competitions_by_season(self, season):
        return self.get_competitions(season=season)

if __name__ == "__main__":
    c = Competition()
    comps = c.get_all_competitions_by_season(2015)
    print(comps)
    print(comps[0].league)
