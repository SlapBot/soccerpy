from soccerpy.modules.Fundamentals.links.competition_links import CompetitionLinks
from soccerpy.modules.Fundamentals.standing import Standing


class CompetitionLeagueTable:
    def __init__(self, data, headers):
        self.headers = headers
        self.links = CompetitionLinks(data['_links'])
        self.league_caption = data['leagueCaption']
        self.matchday = data['matchday']
        self.standing = Standing(data['standing'])
