from soccerpy.modules.Fundamentals.fixtures import Fixtures


class CompetitionFixtures:
    def __init__(self, data, headers):
        self.headers = headers
        self.links = Links(data['_links'])
        self.count = data['count']
        self.fixtures = Fixtures(data['fixtures'])


class Links:
    def __init__(self, links):
        self.url = links['self']['href']
        self.competition = links['competition']['href']
