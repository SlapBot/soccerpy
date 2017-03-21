from soccerpy.modules.Fundamentals.standing import Standing


class CompetitionLeagueTable:
    def __init__(self, data, headers):
        self.headers = headers
        self.links = Links(data['_links'])
        self.league_caption = data['leagueCaption']
        self.matchday = data['matchday']
        self.standing = Standing(data['standing'])


class Links:
    def __init__(self, links):
        self.url = links['url']['href']
        self.competition = links['competition']['href']
