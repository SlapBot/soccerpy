from soccerpy.modules.Fundamentals.fixtures import Fixtures
from soccerpy.modules.Fundamentals.links.team_links import TeamLinks


class TeamFixtures:
    def __init__(self, data, headers):
        self.headers = headers
        self.links = TeamLinks(data['_links'])
        if 'timeFrameStart' in data:
            self.time_frame_start = data['timeFrameStart']
        if 'timeFrameEnd' in data:
            self.time_frame_end = data['timeFrameEnd']
        self.count = data['count']
        self.fixtures = Fixtures(data['fixtures'])
